# -*- coding: utf-8 -*-
from realestatescraper.items import RealestatescraperItem
from scrapy import Request, Spider


class HousingSpider(Spider):
    name = "housing"
    allowed_domains = ["www.homegate.ch"]
    start_urls = [
        # 'https://www.homegate.ch/buy/house/region-lausanne/matching-list?tab=list&o=sortToplisting-desc'
        'https://www.homegate.ch/buy/house/'
        'surrounding-city-lausanne/'
        'matching-list?tab=list&o=sortToplisting-desc&be=15000'
    ]

    def parse(self, response):
        """Parses the websites listed in start_urls.

        This is the default callback used by Scrapy
        to process downloaded responses, when their requests don’t
        specify a callback. It is executed
        with the command 'scrapy crawl --nolog housing'.

        Args:
            response: the response to parse

        Returns:
            yields pages to parse
        """

        # Retrieve data from the detail subpages
        item_links = response.css('.detail-page-link::attr(href)').extract()
        for href in item_links:
            print(href)
            yield response.follow(href, self.parse_detail_page)

            # Proceed to the next page of search results
            next_page = response.css('li.next a::attr(href)').extract_first()
            if next_page is not None:
                next_page = response.urljoin(next_page)
                yield Request(next_page, callback=self.parse)

    def parse_detail_page(self, response):
        """Parses detail pages of individual listings.

        Args:
            response: the response to parse

        Returns:
            yields RealestatescraperItem()
        """

        def extract_with_css(query):
            return response.css(query).extract_first(default='NaN').strip()

        def extract_with_property(prop):
            # Example:
            # response.xpath('//span[@itemprop="price"]/text()')[0].extract()
            return response.xpath(
                '//span[@itemprop="' + prop + '"]/text()'
            ).extract_first(default='NaN').strip()

        def extract_main_features(query):
            keys = response.css(query).xpath(
                '*/li').css('.text--small::text').extract()
            values = response.css(query).xpath(
                '*/li').css('.float-right::text').extract()
            assert len(keys) == len(values)
            return dict(zip(keys, values))

        def extract_main_feature(feature):
            """
            This is preferred over the extract_main_features
            due to that the other method cannot correctly deal
            with return values like
            <span>120</span> m<sup>2</sup>

            Example:
            response.xpath('string(*//li[contains(., "Living space")])')
              .extract_first().strip().split('\n')
            Returns: ['Living space', '120 m2']
            """
            result = response.xpath(
                'string(*//li[contains(., "'
                + feature
                + '")])'
            ).extract_first(default='NaN').strip().split('\n')
            if len(result) > 1:
                return result[1]
            else:
                return 'NaN'

        item = RealestatescraperItem()
        item['url'] = response.url
        item['location'] = extract_with_css('.detail-address-link>span::text')
        item['price'] = extract_with_property('price')
        main_features = [
            'Type',
            'Rooms',
            'Living space',
            'Lot size',
            'Volume',
            'Year built',
            'Available']
        for feat in main_features:
            item[feat.lower().replace(' ', '_')] = extract_main_feature(feat)
        yield item

    def main():
        pass

    if __name__ == '__main__':
        main()
