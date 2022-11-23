#!/usr/bin/python

# Import packages
import numpy as np
import pandas as pd
import os

# Positive

path = 'norsentlex/Fullform'
for file in os.listdir(path):
    if 'Positive.json' in file:
        pos = pd.read_json(str(path+'/'+file), orient='index')
print(pos)        
# Negative
