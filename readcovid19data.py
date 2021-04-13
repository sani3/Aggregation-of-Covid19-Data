import os
import pandas as pd
import numpy as np

# all_data is the variable with all the covid19 Data
def readdata():
    dir = "Dataset/COVID-19-master/csse_covid_19_data/csse_covid_19_daily_reports/"
    all_data = pd.DataFrame()
    files_to_read = os.listdir(dir)[1:-1]

    for i in range(len(files_to_read)):
        file_name = files_to_read[i]
        a = pd.read_csv(dir + file_name)
        # Similar fields have different names in different files
        # We need to renmae the offending field names for consistency
        a.rename({'Country/Region': 'Country_Region',
                  'Province/State': 'Province_State',
                  'Last Update': 'Last_Update',
                  'Lat': 'Latitude',
                  'Long_': 'Longitude'}, axis=1, inplace=True)
        a["Date"] = file_name.split(".")[0]
        all_data = pd.concat([all_data, a], axis=0)  # all_data = all_data.append(a)

    # all_data['Last_Update'] = all_data['Last_Update'].apply(lambda x: x.replace('T', ' '))
    # all_data['Date'] = all_data['Last_Update'].apply(lambda x: x.split(' ')[0])
    #all_data.to_csv("allcovid19data.csv")
    #Comfirm output is as expected.
    return all_data

