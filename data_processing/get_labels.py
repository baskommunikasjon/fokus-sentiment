#!/usr/bin/python

# Import packages
import numpy as np
import pandas as pd
import os
import json
from ast import literal_eval
import openpyxl


def get_positive_and_negative_words():
    path = 'norsentlex/Fullform'
    for file in os.listdir(path):
        # Positive
        if 'Positive.json' in file:
            pos = pd.read_json(str(path+'/'+file), orient='index')
            pos_explode_fixed = pos.apply(pd.Series.explode).reset_index()
            # Save result as an excel to check if explode worked
            pos_explode_fixed.rename(columns={'index':'Word'}, inplace=True)
            print(pos_explode_fixed)  
            pos_explode_fixed.to_excel('data/Positive words.xlsx')
        # Negative
        elif 'Negative.json' in file:
            neg = pd.read_json(str(path+'/'+file), orient='index')
            neg_explode_fixed = neg.apply(pd.Series.explode).reset_index()
            neg_explode_fixed.rename(columns={'index':'Word'}, inplace=True)
            print(neg_explode_fixed)  
            neg_explode_fixed.to_excel('data/Negative words.xlsx')
    return pos_explode_fixed, neg_explode_fixed 
