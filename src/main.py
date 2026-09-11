from ingestion.reader import load_data
from profiling.profiler import profile_data
def main():
    file_path = './data/input/patients_records.csv'
    print("Pipeline starting...")
    #print(load_data(file_path))
    data = load_data(file_path)
    data['gender'] = data['gender'].str.lower()
    print(data['gender'])

    gender_map = { 'm': 'Male',
                   'male': 'Male',
                   'f': 'Female',
                   'female': 'Female'}
    data['gender'] = data['gender'].map(gender_map)
    print(data['gender'].value_counts())

    print(data['date_of_birth'])

if __name__ == "__main__":
    main()