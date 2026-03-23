from extract import extract_data
from transform import transform_data
from load import load_data

def run_pipeline():

    print("Starting ETL Pipeline...")

    df = extract_data()

    df = transform_data(df)

    load_data(df)

    print("ETL Pipeline Finished!")

if __name__ == "__main__":
    run_pipeline()