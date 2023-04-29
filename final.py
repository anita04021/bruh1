import sqlite3
import pandas as pd
import streamlit as st

# create a connection to the database
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



conn = sqlite3.connect('ecsel_database.db')
new_participants = '''SELECT country, shortName, name, activityType, organizationURL, SUM(ecContribution) 
           FROM participants
           GROUP BY country
           ORDER BY SUM(ecContribution) DESC'''
df_participants = pd.read_sql_query(new_participants, conn)

conn.close()
print(df_participants)

st.dataframe(df_participants) 

                    
