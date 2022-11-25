#!/usr/bin/python

# Import packages
import pandas as pd
import xlsxwriter

# Functions
def save_excel(df1, df2,filename,sheetname_1, sheetname_2):
    writer = pd.ExcelWriter(f'data/{filename}.xlsx', 
                            engine ='xlsxwriter')
    if len(df1)>1:
        try:
            df1.to_excel(writer, sheet_name=sheetname_1)
        except Exception:
            pass
        try:
            df2.to_excel(writer, sheet_name=sheetname_2)
        except Exception:
            pass
    elif len(df1)==0:
        pass
    writer.close()