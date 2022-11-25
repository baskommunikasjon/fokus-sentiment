#!/usr/bin/python

# Import packages
import pandas as pd

# Functions
def save_excel(df1, df2, sheetname_1, sheetname_2):
    writer = pd.ExcelWriter('data/.xlsx', 
                            engine ='xlsxwriter')
    
    df1.to_excel(writer, sheet_name=sheetname_1)
    df2.to_excel(writer, sheet_name=sheetname_2)
    writer.close()