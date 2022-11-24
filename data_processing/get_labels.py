#!/usr/bin/python

# Import packages
import numpy as np
import pandas as pd
import os
import json
from ast import literal_eval
import openpyxl
# Positive

path = 'norsentlex/Fullform'
for file in os.listdir(path):
    if 'Positive.json' in file:
        pos = pd.read_json(str(path+'/'+file), orient='index')
        pos_explode_fixed = pos.apply(pd.Series.explode).reset_index()
        
        

print(pos)   
print(pos_explode_fixed)   
#print(fixed_dataframe) 
#print(fixed_dataframe)
# Save result as an excel to check if explode worked
pos_explode_fixed.to_excel('data/Positive words.xlsx')
# Negative
