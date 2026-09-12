import pandas as pd

def clean_data(df):

    df = clean_gender(df)

    #fixing the date 
    df['date_of_birth'] = df['date_of_birth'].apply(clean_date)
    df['date_of_birth'] = pd.to_datetime(df['date_of_birth'])

    #fixing names
    df['name'] = df['name'].apply(clean_names)
    df['name'] = df['name'].str.title()
    

    return df


#*****************Cleaning the genders************************#
def clean_gender(df):
    df['gender'] = df['gender'].str.lower()
    gender = { 'male': 'Male',
               'm': 'Male',
               'female': 'Female',
               'f': 'Female'}
    df['gender'] = df['gender'].map(gender)
    
    return df


#***************Cleaning the dates of birth******************#
def clean_date(date):

    new_date = date.replace('/', '-').split('-')

    if len(new_date[0]) == 2:
        new_date = new_date[::-1]

    return '-'.join(new_date)
       

def clean_names(name):

    clean_name = name.split()
    return ' '.join(clean_name)
