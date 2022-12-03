import pandas as pd
import numpy as np
import pdb

dataset = pd.read_csv("../NYPD_Complaint_Data_Historic.csv", low_memory=False)
dataset.drop(columns = ['CMPLNT_NUM', 'PD_CD', 'KY_CD', 'HOUSING_PSA', 'PARKS_NM', 'TRANSIT_DISTRICT', 'STATION_NAME' ,'HADEVELOPT'], inplace = True)
pdb.set_trace()