#!/usr/bin/python

# Import packages
import numpy as np
import pandas as pd
import os
import json
from ast import literal_eval
# Positive

path = 'norsentlex/Fullform'
for file in os.listdir(path):
    if 'Positive.json' in file:
        pos = pd.read_json(str(path+'/'+file), orient='index')
        #pos = json.loads(file) 
        '''- it does not work. This contains
         an error '''
        pos_explode = pos['forms'].apply(pd.Series)
        fixed_columns = []
        for col in pos_explode.columns:
            #pos_explode_fixed = pos_explode[col].apply(pd.Series)
            pos_explode_fixed = pos_explode[col].explode()
            fixed_columns.append(pos_explode_fixed)
        fixed_dataframe = pd.concat(fixed_columns)
        #fixed_dataframe = pd.concat(fixed_columns)
        

print(pos)   
print(pos_explode)   
print(fixed_dataframe) 
#print(fixed_dataframe)
# Save result as an excel to check if explode worked

# Negative
