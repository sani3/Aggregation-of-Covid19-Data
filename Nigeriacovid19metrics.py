import pandas as pd
import numpy as np
from readcovid19data import readdata

#get data
all_data = readdata()
all_country = all_data.groupby('Country_Region')
nigeria_data = all_country.get_group('Nigeria')
nigeria_data = nigeria_data[['Last_Update', 'Date', 'Confirmed', 'Deaths', 'Recovered', 'Active']]
nigeria_data = nigeria_data.groupby('Last_Update')
ndf = nigeria_data.apply(lambda x: x.iloc[0])
ndf = ndf.sort_values(by='Date', ascending=True)

# ndf['dDate'] = ndf['Date'].apply(lambda x: x.split('-')[1]).astype(np.int)
# ndf['mDate'] = ndf['Date'].apply(lambda x: x.split('-')[0]).astype(np.int)
# ndf.sort_values(by=['mDate', 'dDate'], ascending=[True, True])



#Total global confirmed cases
nigeria_confirmed_cases = ndf['Confirmed'].max()
print('Confirmed cases of covid19 in Nigeria: {}'.format(nigeria_confirmed_cases))

#Total global deaths with Covid19
nigeria_deaths = ndf['Deaths'].max()
print('Deaths with covid19 in Nigeria: {}'.format(nigeria_deaths))

#Percentage of confirmed cases that died
PDC = (nigeria_deaths/nigeria_confirmed_cases)*100
print('Percentage of confirmed cases that died in Nigeria: {}%'.format(PDC))

#Total global cases recovered from covid19
nigeria_recoveries = ndf['Recovered'].max()
print('Recoveries from covid19 in Nigeria: {}'.format(nigeria_recoveries))

#Percentage of confirmed cases that recovered
PRC = (nigeria_recoveries/nigeria_confirmed_cases)*100
print('Percentage of confirmed cases that recovered in Nigeria: {}%'.format(PRC))

#Number of active cases
nigeria_active_cases = nigeria_confirmed_cases - (nigeria_deaths + nigeria_recoveries)
print('Number of active cases with covid19 in Nigeria: {}'.format(nigeria_active_cases))


#Percentage of active cases
PAC = (nigeria_active_cases/nigeria_confirmed_cases)*100
print('Percentage of active cases in Nigeia: {}%'.format(PAC))



# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# ax.plot(ndf.loc[:, 'Confirmed'], label='Confirmed cases')
# ax.plot(ndf.loc[:, 'Deaths'], label='Deaths')
# ax.plot(ndf.loc[:, 'Recovered'], label='Recovered cases')
# ax.plot(ndf.loc[:, 'Active'], label='Active cases')
# ax.set_title("Title")
# ax.set_xlabel("Date")
# ax.set_ylabel("Cumulative count")
# ax.legend()