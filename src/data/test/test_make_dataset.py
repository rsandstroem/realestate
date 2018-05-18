from data import make_dataset
import pandas as pd


def test_process_columns():
    df = pd.DataFrame(index=[0],
                      data={
                          "url": "https://www.homegate.ch/buy/108397869",
                          "location": "1113 St-Saphorin-sur-Morges",
                          "price": "1,250,000.\u2013",
                          "type": "Single house",
                          "rooms": "4.5",
                          "living_space": "150 m2",
                          "lot_size": "335 m2",
                          "volume": "NaN",
                          "year_built": "NaN",
                          "available": "by agreement"
                      })
    make_dataset.process_columns(df)
    assert df.url[0] == "https://www.homegate.ch/buy/108397869"
