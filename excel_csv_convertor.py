# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 12:22:25 2023

@author: Marketpulse
"""

import polars as pl
import streamlit as st
import pandas as pd

file_upld=st.file_uploader("Please Upload The Excel File!")
file_name=file_upld.name
pl_df=pl.read_excel(file_upld,sheet_name='CSV')
df=pl_df.to_pandas()
df['PERIOD']=pd.to_datetime(df['PERIOD'])
csv_df=df.to_csv(index=False,date_format="%d-%m-%Y")

st.download_button(
    label="Download data as CSV",
    data=csv_df,
    file_name=file_name+".csv",
    mime='text/csv',
)



