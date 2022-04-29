#!/usr/bin/env python
# coding: utf-8

# In[1]:


import streamlit as st
import pandas as pd
import numpy as np
accidents_df = pd.read_csv('aircraft_accidents_excel.csv')
aircraft_manu = pd.read_csv('Make Fatalities 1989-2018.csv')



# In[2]:





# In[3]:





# In[4]:


aircraft_manu[['ManuF','ManuL']] = aircraft_manu['Make'].str.split(' ',n=1,expand=True)
aircraft_manu.ManuF= aircraft_manu.ManuF.str.lower()



# In[5]:


accidents_df[['ManuF', 'Registration']] = accidents_df['Model'].str.split(' ',n=1,expand=True)
accidents_df.ManuF=accidents_df.ManuF.str.lower()



# In[6]:


aircraft_data = accidents_df.merge(aircraft_manu,how='left',on='ManuF')
aircraft_data = aircraft_data.drop(columns=['Total Fatalities','ManuL','ManuF'])
aircraft_data = aircraft_data[aircraft_data['Percentage'].notna()]



# In[7]:




st.title('Aircraft Accidents 2018-2022')
choice = st.sidebar.selectbox("Manufacturer",aircraft_data.Make.unique())

choice_manu = aircraft_data[aircraft_data['Make']==choice]
choice_manu
loc = choice_manu[['lat','lon']]
st.map(loc)
st.write("[Deepnote Code](https://deepnote.com/workspace/elbin-rojas-8c4a-d0bbe724-bfed-4f88-8960-a4bdd8cc5fde/project/MA-346-Final-Project-174ece8e-9da1-4371-a2cd-1c30546a5476/%2FMA-346-Final-Project%2Fnotebook.ipynb)")
st.write("[Project Report](https://bentleyedu-my.sharepoint.com/:w:/g/personal/rojas_elbi_bentley_edu/EfUfhVoXJlBNlfoEL2uFW8wBpXTgo-Z6Cx_XmPumQ_JQ5A?e=7rALTS)")
st.write("[Github Repository](https://github.com/elbin-167/MA-346-Final-Project)")


# create a number range for the percentages and use the choice_manu as a basis for dividing the ranges

