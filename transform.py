def transform_data(df):

    print("Dataset Shape:", df.shape)

    print("Fraud vs Normal Transactions:")
    print(df["Class"].value_counts())

    return df