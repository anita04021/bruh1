#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 27 14:44:36 2023

@author: anitabaculima
"""
import sqlite3
import pandas as pd
import streamlit as st

# create a connection to the database
conn = sqlite3.connect('ecsel_database.db')
query = "SELECT Country, Acronym FROM countries"
df_countries = pd.read_sql(query, conn) 
conn.close()

country_dict = dict(zip(df_countries["Acronym"], df_countries["Country"]))

print(country_dict)
 
st.selectbox('Select a Country:',df_countries["Acronym"]) 


                        