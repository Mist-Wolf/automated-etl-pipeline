from ingestion.reader import load_data
import pandas as pd
from transformation.transform import clean_data
from profiling.profiler import profile_data

def main():
    file_path = './data/input/patients_records.csv'
    print("Pipeline starting...")
    #print(load_data(file_path))
    df = load_data(file_path)
    print(clean_data(df))
    print(df.dtypes)



if __name__ == "__main__":
    main()