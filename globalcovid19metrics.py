import pandas as pd
import numpy as np
from readcovid19data import readdata

#get data
all_data = readdata()

#Total global confirmed cases
global_confirmed_cases = all_data['Confirmed'].sum()
print('Global confirmed cases of covid19 is {}'.format(global_confirmed_cases))

#Total global deaths with Covid19
global_deaths = all_data['Deaths'].sum()
print('Global deaths with covid19 is {}'.format(global_deaths))

#Percentage of confirmed cases that died
PDC = (global_deaths/global_confirmed_cases)*100
print('Percentage of confirmed cases that died is {}%'.format(PDC))

#Total global cases recovered from covid19
global_recoveries = all_data['Recovered'].sum()
print('Global recoveries from covid19 {}'.format(global_recoveries))

#Percentage of confirmed cases that recovered
PRC = (global_recoveries/global_confirmed_cases)*100
print('Percentage of confirmed cases that recovered is {}%'.format(PRC))

#Number of active cases
global_active_cases = global_confirmed_cases - (global_deaths + global_recoveries)
print('Global number of active cases with covid19 is {}'.format(global_active_cases))

#Percentage of active cases
PAC = (global_active_cases/global_confirmed_cases)*100
print('Percentage of active cases is {}%'.format(PAC))
