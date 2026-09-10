from ingestion.reader import load_data
from profiling.profiler import profile_data
def main():
    file_path = './data/input/patients_records.csv'
    print("Pipeline starting...")
    #print(load_data(file_path))
    data = load_data(file_path)
    profile_data(data)

if __name__ == "__main__":
    main()