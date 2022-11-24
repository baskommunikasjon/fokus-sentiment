#!/usr/bin/python

# Import packages
import numpy as np
import pandas as pd
import os
import json

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
            pos_explode_fixed = pos_explode.explode(col)
            fixed_columns.append(pos_explode_fixed)
        fixed_dataframe = pd.concat(fixed_columns)
        full_fixed = []
        for col in fixed_dataframe.columns:
            fixed_dataframe_col = fixed_dataframe.explode(col)
            full_fixed.append(fixed_dataframe_col)
        final_fix = pd.concat(full_fixed)

print(pos)   
print(pos_explode)    
print(fixed_dataframe)
print(full_fixed)
# Negative
