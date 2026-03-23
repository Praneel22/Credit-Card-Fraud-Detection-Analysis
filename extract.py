import pandas as pd

def extract_data():

    df = pd.read_csv("data/Raw/creditcard.csv")

    print("Data extracted successfully")
    print(df.head())

    return df