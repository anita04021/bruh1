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

conn = sqlite3.connect('ecsel_database.db')
new_participants = '''SELECT country, shortName, name, activityType, organizationURL, SUM(ecContribution) 
           FROM participants
           ORDER BY SUM(ecContribution) DESC'''
df_participants = pd.read_sql_query(new_participants, conn)
df_participants = df_participants.rename(columns={'country': 'Acronym'})

conn.close()

print(df_participants)

options = df_participants['Acronym'].unique().tolist()
selected_country = st.selectbox('Select a Country:', options) 
filtered_df = df_participants[df_participants['Acronym'] == selected_country]

st.write('Filtered dataframe:')
st.write(filtered_df)


                    