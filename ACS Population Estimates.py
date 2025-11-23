#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 10 20:41:42 2025

@author: corinamccullough
"""

# https://pygis.io/docs/d_access_census.html
# Variables list: https://api.census.gov/data/2020/acs/acs5/variables.html
# https://censusdis.readthedocs.io/en/1.1.3/intro.html

import pandas as pd
from census import Census
import time
import numpy as np


api_key = "041f118e070667dea491978da5e7c2bedb842535"
c = Census(api_key)

# 2024 Data will release December 11, 2025

# Extract 2023 5-year population estimates
year = 2023
data = c.acs5.get(('NAME', "B15003_023E"), {'for': 'state:*'}, year = year)
data = pd.DataFrame.from_dict(data)
data.columns = ['State','Population','FIPS']
total_2023 = data['Population'].sum()
total_2023 = pd.DataFrame([total_2023], columns=['Population'])
total_2023['Year'] = year


# Extract multiple 5-year population estimates
year = ['2013','2014','2015','2016','2017','2018','2019','2020','2021','2022','2023']

acs_data = []

for y in year:
    year = int(y)
    acs = c.acs5.get(('NAME', "B01003_001E"), {'for': 'state:*'}, year = year)
    data = pd.DataFrame.from_dict(acs)
    data.columns = ['State','Population','FIPS']
    total = data['Population'].sum()
    total = pd.DataFrame([total], columns=['Population'])
    total['Year'] = y
    acs_data.append(total)
    print(f"Finished extracting {y} ACS population 5-year estimates.")
    lag = np.random.uniform(1,5) # every 1 to 5 seconds
    time.sleep(lag) 
print(f'Task Completed.')

acs_data = pd.concat(acs_data, ignore_index=True)









