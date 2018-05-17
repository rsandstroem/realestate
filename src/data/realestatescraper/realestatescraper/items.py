# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class RealestatescraperItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()
    location = scrapy.Field()
    price = scrapy.Field()
    type = scrapy.Field()
    rooms = scrapy.Field()
    living_space = scrapy.Field()
    lot_size = scrapy.Field()
    volume = scrapy.Field()
    year_built = scrapy.Field()
    available = scrapy.Field()
