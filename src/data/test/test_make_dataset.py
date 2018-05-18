from data import make_dataset
import pandas as pd
import numpy as np


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
                          "year_built": "1999",
                          "available": "by agreement"
                      })
    make_dataset.process_columns(df)
    assert df.url[0] == "https://www.homegate.ch/buy/108397869" # unchanged
    assert df.commune[0] == "St-Saphorin-sur-Morges" # substring
    assert df.postal_code[0] == "1113" # substring
    assert df.price[0] == 1250000. # float
    assert df.type[0] == "Single house" # unchanged
    assert df.rooms[0] == 4.5 # float
    assert df.living_space[0] == 150. # substring as float
    assert df.lot_size[0] == 335. # substring as float
    assert np.isnan(df.volume[0]) # survive NaN in source data
    assert df.year_built[0] == 1999. # float
    assert df.available[0] == "by agreement" # unchanged



