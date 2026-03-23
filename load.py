def load_data(df):

    df.to_csv("data/Processed/processed_data.csv", index=False)

    print("Processed data saved successfully")