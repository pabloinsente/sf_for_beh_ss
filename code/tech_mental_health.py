#!/usr/bin/env python
# coding: utf-8

# # Mental Health Survey in Tech - Data Exploration and Cleaning

# This dataset is from a 2014 survey that measures attitudes towards mental health and frequency of mental health disorders in the tech workplace.  
# **Source**: https://www.kaggle.com/osmi/mental-health-in-tech-survey

# In[1]:


import pandas as pd
import altair as alt
alt.themes.enable('latimes')
#get_ipython().run_line_magic('load_ext', 'watermark')
#get_ipython().run_line_magic('watermark', '--iversions -w -v -u -d -m')


# ## Read data in

# In[2]:


tech = pd.read_csv('../data/mental_health_tech_data.csv', sep=',')
tech.head(2)


# ## Dataset metadata

# In[3]:


tech.info()


# ## Dataset missing values

# In[4]:


tech.isnull().sum()


# In[5]:


tech_d = tech.dropna(axis='columns')
tech_d.shape


# In[6]:


tech_d.head(2)


# In[7]:


tech_d.isnull().sum()


# ## Select and clean features

# In[8]:


# we will drop some features because require too much pre-processing for our current purposes
# TL;DR: ain't nobody got time for that
to_drop = ['Timestamp', 'no_employees', 'Gender', 'Country'] 
tech_d = tech_d.drop(to_drop, axis=1)


# In[9]:


# we reduced the dataset to 19 features
tech_d.shape 


# In[10]:


# we have only one quantitative variable
tech_d.describe()


# ## 

# The values of age do not make sense. Looks like wehave negative values and values over 100
# Let's clean that up a bit

# In[11]:


# keep ages <= 100 AND >= 15
tech_d = tech_d[(tech_d['Age'] <= 100) & (tech_d['Age'] >= 15)] 
tech_d.describe()


# In[12]:


# check balance of target feature
tech_d['treatment'].value_counts()


# ## Explore variables

# In[13]:


# for real value variables histograms work great
hist_1 = alt.Chart(tech_d).mark_bar().encode(
    x='Age',
    y='count()')
hist_1


# In[14]:


# for categorical variables we use counts is a good idea
bar_1 = alt.Chart(tech_d).mark_bar().encode(
    x='count()',
    y='treatment:N')
bar_1


# At this point we realize that we need to create a reusable function if we want to continue doing multiple similar plots. this is what we call **'refactoring'** the code. 

# In[15]:


def plot_cat(variable: str) -> 'Chart':
    '''plot categorical variables
    Parameters:
    variable: variable name 
    ---
    Returns:
    Altair bar chart
    '''
    chart = alt.Chart(tech_d).mark_bar().encode(
        x='count()',
        y=variable,
        color=alt.Color(variable, legend=None))
    return chart


# In[16]:


# we can concatenate charts together pretty easily
panel_chart1 = (plot_cat('family_history') | plot_cat('remote_work')) & (plot_cat('care_options')  | plot_cat('anonymity')) 
panel_chart1


# Now let's plot the same variables grouped by treatment (target).

# In[17]:


bar_2= alt.Chart(tech_d).mark_bar().encode(
    x='count()',
    y='family_history',
    color='treatment')
bar_2


# Nice, now we can refactor the code as before to make multiple plots.

# In[18]:


def plot_grouped_cat(variable:str)-> 'Chart':
    chart =alt.Chart(tech_d).mark_bar().encode(
        x='count()',
        y=variable,
        color=alt.X('treatment:N'))
    return chart


# In[19]:


panel_chart2 = (plot_grouped_cat('family_history') | plot_grouped_cat('remote_work')) & (plot_grouped_cat('care_options') | plot_grouped_cat('anonymity'))
panel_chart2


# ## Save our figures

# In[20]:


from datetime import date
date_stamp = date.today().strftime('%Y-%b-%d')
path = '../results'
hist_1.save(f'{path}/hist_1_{date_stamp}.png')
bar_1.save(f'{path}/bar_1_{date_stamp}.png')
bar_2.save(f'{path}/bar_2_{date_stamp}.png')
panel_chart1.save(f'{path}/panel_chart_1_{date_stamp}.png')
panel_chart2.save(f'{path}/panel_chart_2_{date_stamp}.png')


# ## Save Data

# In[21]:


path = '../data'
tech_d.to_csv(f'{path}/mental_health_tech_data_post{date_stamp}.csv')

