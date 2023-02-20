import pandas as pd

def get_dataset():
    dataset = pd.read_csv("../NYPD_Complaint_Data_Historic.csv", low_memory=False)
    dataset.drop(columns = ['CMPLNT_NUM', 'PD_CD', 'KY_CD', 'HOUSING_PSA', 'PARKS_NM', 'TRANSIT_DISTRICT', 'STATION_NAME' ,'HADEVELOPT'], inplace = True)

    return dataset

def print_name():
    print("New York City Crime Dataset")

