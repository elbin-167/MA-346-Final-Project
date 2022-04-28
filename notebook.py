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


from IPython.display import HTML
import os
# def get_list(start,stop,set1):
#     empty_list = []
#     a = np.arange(start,stop,set1)
#     for i in a:
#         empty_list.append(i)
#     return empty_list


# dic = {"0-25%": get_list(0,0.25,0.000001),        
#         "25-50%": get_list(0.25,0.5,0.000001),
#         "50-75%": get_list(0.5,0.75,0.000001),
#         "75-100%": get_list(0.75,1,0.000001),
#         }
st.title('Aircraft Accidents 2018-2022')
choice = st.sidebar.selectbox("Manufacturer",aircraft_data.Make.unique())

choice_manu = aircraft_data[aircraft_data['Make']==choice]
choice_manu
loc = choice_manu[['lat','lon']]

st.map(loc)


# create a number range for the percentages and use the choice_manu as a basis for dividing the ranges

