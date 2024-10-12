import pandas as pd
import numpy as np
import streamlit as st
import pandaslib as pl
  
'''
For each file you extract save it in .csv format with a header to the cache folder. 
The basic process is to read the file, add lineage, then write as a .csv to the cache folder.
Extract the states with codes google sheet. Save as cache/states.csv
Extract the survey google sheet, and engineer a year column from the Timestamp using the extract_year_mdy function in pandaslib.py. 
Then save as cache/survey.csv
For each unique year in the surveys: extract the cost of living for that year from the website, engineer a year column for that year, 
then save as cache/col_{year}.csv for example for 2024 it would be cache/col_2024.csv

link for survey sheet: https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/edit?resourcekey=&gid=1625408792#gid=1625408792
csv download version link: https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?resourcekey=&gid=1625408792&format=csv

ln pandaslib l have these functions: clean_currency, extract_year_mdy, clean_country_usa
'''

url = "https://docs.google.com/spreadsheets/d/1IPS5dBSGtwYVbjsfbaMCYIWnOuRmJcbequohNxCyGVw/export?format=csv"
df = pd.read_csv(url, header=0, index_col=0)

# engineer a year column from the Timestamp using the extract_year_mdy function
df['year'] = df['Timestamp'].apply(pl.extract_year_mdy)

# save as cache/survey.csv
df.to_csv('cache/survey.csv')

# unique year in the surveys
years = df['year'].unique()

# extract the cost of living for that year from the website, engineer a year column for that year
for year in years:
    url = f"https://www.numbeo.com/cost-of-living/rankings.jsp?title={year}&region=1"
    df = pd.read_html(url)[0]
    df['year'] = year
    df.to_csv(f'cache/col_{year}.csv')


