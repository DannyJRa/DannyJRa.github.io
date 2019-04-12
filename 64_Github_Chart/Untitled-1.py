#%% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting
import os
try:
	os.chdir(os.path.join(os.getcwd(), '64_Github_Chart'))
	print(os.getcwd())
except:
	pass


#%%
# An example to get the remaining rate limit using the Github GraphQL API.

import requests

# main_with_json.py
import json
   
# The GraphQL query (with a few aditional bits included) itself defined as a multi-line string.       
#%%

github=open('github.json', 'r').read()
json.dumps(github,indent=4)


#%%
test=map(lambda x: x['data'], github)
print(test)


# Read json file
#%%
with open("github.json", "r") as read_file:
    data=json.load(read_file)


## Function to map variables

#%%
# recursivejson.py

def extract_values(obj, key):
  
    arr = []

    def extract(obj, arr, key):
     
        if isinstance(obj, dict):
            for k, v in obj.items():
                if isinstance(v, (dict, list)):
                    extract(v, arr, key)
                elif k == key:
                    arr.append(v)
        elif isinstance(obj, list):
            for item in obj:
                extract(item, arr, key)
        return arr

    results = extract(obj, arr, key)
    return results



#%%
from dateutil.parser import parse

datetime = parse('2018-06-29 22:21:41')
datetime.date()
datetime.time()
print(datetime)
print(datetime.timestamp())


#%%

dates=extract_values(data,'date')
type(dates)

#%%
from dateutil.parser import parse

# Loop

#Map

dates2=list(map(parse,dates))

print(dates2)

#List comprehension
#dates3=[parse(x) for x in dates]
#dates3=[x.timestamp() for x in dates3]
#dates3=[x.date() for x in dates3]
import datetime as dt
dates3=[dt.datetime.strptime(x, "%Y-%m-%dT%H:%M:%S%z") for x in dates]

print(dates3)




#How do I translate an ISO 8601 datetime string into a Python datetime object? [duplicate]#
#%%
test=dt.datetime.strptime(dates[1], "%Y-%m-%dT%H:%M:%S%z")
print(test.date())
#%%


from datetime import datetime





#%%





headline=extract_values(data,'messageHeadline')
print(headline)




#Create Dataframe
#%%
import pandas as pd
import numpy as np

data=pd.DataFrame(data=
    {'dates':dates3,
    'headline': headline
    })
data.dtypes
data
#%%
# Aggregation
#import datetime as dt
#data['month']=pd.to_datetime(data['dates']).dt.to_period('M')
#data
data['dates']=data['dates'].dt.tz_localize('US/Eastern')
#data['dates']=pd.to_datetime(data['dates'])
data.pivot_table(index='dates',aggfunc='count')

#%%
df=data
df['datetime'] = pd.to_datetime(df['dates'])
df = df.set_index('datetime')
df.drop(['dates'], axis=1, inplace=True)
df.head()
data.groupby(lambda x: x.date).count()
#data['dates2']=data['dates'].dt.year

#%%
#We can convert the strings to timestamps by inferring their format, then look at the values:
timestamp_date_rng = pd.to_datetime(dates, infer_datetime_format=True)
timestamp_date_rng

x = pd.Series(headline, index = timestamp_date_rng)

x.groupby(lambda x: x.date).count()




x = x.rename_axis(['index1']).reset_index()

x
#%%
#Back to timestamp
#Convert pandas DateTimeIndex to Unix Time?



#%%
#Save to json
#final=x.set_index('index1').rename(columns={'0':'index1'}).to_json()


#x.set_index('index1').rename(columns={'0':'index1'}).to_json('file.json')
x.set_index('index1').to_json('file.json')



#%%
# Create date and time with dataframe 
rng = pd.DataFrame() 
rng['date'] = pd.date_range('1/1/2011', periods = 72, freq ='H') 

# Print the dates in dd-mm-yy format 
rng[:5] 

# Create features for year, month, day, hour, and minute 
rng['year'] = rng['date'].dt.year 
rng['month'] = rng['date'].dt.month 
rng['day'] = rng['date'].dt.day 
rng['hour'] = rng['date'].dt.hour 
rng['minute'] = rng['date'].dt.minute 

# Print the dates divided into features 
rng.head(3) 


#%%
###Save json
with open('github_test.json', 'w') as f:  # writing JSON object
    json.dump(final, f,indent=4)

#%%
