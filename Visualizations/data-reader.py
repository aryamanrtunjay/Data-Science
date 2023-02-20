import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("../NYPD_Complaint_Data_Historic.csv")
"""Drop unnecessary columns"""
dfcrime = df.copy()
#dfcrime = dfcrime.loc[1:10000]
dfcrime.drop(['JURIS_DESC', 'ADDR_PCT_CD', 'PARKS_NM', 'HADEVELOPT', 'X_COORD_CD', 'Y_COORD_CD',
              'Latitude', 'Longitude', 'Lat_Lon', 'LOC_OF_OCCUR_DESC',
              'KY_CD', 'PD_CD', 'PD_CD'], axis=1, inplace=True)
dfcrime.columns
dfcrime.columns = ['CMPLT_NUM', 'CMPLNT_FR_DT','CMPLNT_FR_TM', 'CMPLNT_TO_DT', 'CMPLNT_TO_TM',
                   'RPT_DT', 'OFNS_DESC', 'PD_DESC', 'CRM_STTUS', 'LAW_CODE',
                   'BORO_NM', 'PREM_TYP_DESC']
dfcrime.head()

df2 = dfcrime.copy()
def eliminate_nonsense_dates(x):
    if x[2] > '2050':
        x = None
    elif x[2] < '2010':
        x = None
    else:
        aa= '/'.join(x)
        return (aa)

df2 = df2.join(df2['LAW_CODE'].str.get_dummies()) #get dummy columns for crime categories
df2.dropna(subset=['CMPLNT_FR_DT'], inplace=True) #drop empty dates
df2['CMPLNT_FR_DT'] = df2['CMPLNT_FR_DT'].str.split("/") #create a list for each value
df2['CMPLNT_FR_DT'] = df2['CMPLNT_FR_DT'].apply(lambda x: eliminate_nonsense_dates(x))

df2['Date_OCCRD'] = df2['CMPLNT_FR_DT'] +' '+df2['CMPLNT_FR_TM'] #Combing date and time columns
df2['Date_OCCRD'] = pd.to_datetime(df2['Date_OCCRD'])
df2.set_index('Date_OCCRD', inplace=True)           #set full date as index

df2.head()

"""Analysis of Violations, Felonies and Misdemeanor"""

dfYear = df2.iloc[:969550] #slice dataframe so it includes only 2014-2015 data
dfYear.index = dfYear.index.year
vis0 = dfYear.groupby([dfYear.index.get_level_values(0)])[['VIOLATION','FELONY','MISDEMEANOR']].sum()
vis0.plot.bar()
plt.title('Amount of crime per year')
plt.xlabel('Year')
plt.show()

dfMonth = df2.iloc[:969550]
dfMonth.index = dfMonth.index.month
vis1 = dfMonth.groupby([dfMonth.index.get_level_values(0)])[['VIOLATION','FELONY','MISDEMEANOR']].sum()
vis1.plot.bar()
plt.title('Amount of crime per month')
plt.legend(loc='upper left')
plt.xlabel('Month')
plt.show()

dfDay = df2.iloc[:969550]
print ("Significantly more crimes happen on the 1st of the month")
dfDay.index = dfDay.index.day
vis2 = dfDay.groupby([dfDay.index.get_level_values(0)])[['VIOLATION','FELONY','MISDEMEANOR']].sum()
vis2.plot.bar(figsize=(12,6))
plt.title('Amount of crime per day')
plt.xlabel('Day of Month')
plt.show()

dfHour = df2.iloc[:969550]
print ("It seems like more crimes happen in the afternoon than at night")
dfHour.index = dfHour.index.hour
vis3 = dfHour.groupby([dfHour.index.get_level_values(0)])[['VIOLATION','FELONY','MISDEMEANOR']].sum()
vis3.plot.bar(figsize=(12,6))
plt.title('Amount of crime per hour')
plt.xlabel('Time of day')
plt.show()
