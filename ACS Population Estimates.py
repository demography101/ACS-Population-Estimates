import pandas as pd
from census import Census
import time
import numpy as np

# You can request Census API key here: https://api.census.gov/data/key_signup.html

api_key = "CENSUS API KEY"
c = Census(api_key)

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









