#!/usr/bin/env python
# coding: utf-8

# # Mental Health Survey in Tech - Data Exploration and Cleaning

# This dataset is from a 2014 survey that measures attitudes towards mental health and frequency of mental health disorders in the tech workplace.  
# **Source**: https://www.kaggle.com/osmi/mental-health-in-tech-survey
# 
# In this workshop we don't have enough time to go through a full tutorial of writing cleaner code, but we will review a few tips:
# 
# - **Tip 1**: Refactoring code for resuability and separation of concerns
# - **Tip 2**: Auto-save artifacts (data, tables, charts, etc) and adding time-stamps  
# 
# **Run cells from 1 to 14 (Tip 1: Refactoring)**

# In[1]:


import pandas as pd
import altair as alt
from datetime import date
#alt.themes.enable('latimes')
get_ipython().run_line_magic('load_ext', 'watermark')
get_ipython().run_line_magic('watermark', '--iversions -w -v -u -d -m')


# ## Read data in

# In[2]:


tech = pd.read_csv('../data/mental_health_tech_data.csv', sep=',')
tech.head(2)


# ## Dataset missing values

# In[3]:


tech.isnull().sum()


# In[4]:


tech_d = tech.dropna(axis='columns')
tech_d.shape


# In[5]:


tech_d.head(2)


# In[6]:


tech_d.isnull().sum()


# ## Select and clean features

# In[7]:


# we will drop some features because require too much pre-processing for our current purposes
to_drop = ['Timestamp', 'no_employees', 'Gender', 'Country'] 
tech_d = tech_d.drop(to_drop, axis=1)


# In[8]:


# we reduced the dataset to 19 features
tech_d.shape 


# In[9]:


# we have only one quantitative variable
tech_d.describe()


# ## 

# The values of age do not make sense. Looks like wehave negative values and values over 100
# Let's clean that up a bit

# In[10]:


# keep ages <= 100 AND >= 15
tech_d = tech_d[(tech_d['Age'] <= 100) & (tech_d['Age'] >= 15)] 
tech_d.describe()


# In[11]:


# check balance of target feature
tech_d['treatment'].value_counts()


# ## Explore variables

# In[12]:


# for real value variables histograms work great
hist_1 = alt.Chart(tech_d).mark_bar().encode(
    x='Age',
    y='count()')
hist_1


# In[13]:


# for categorical variables we use counts is a good idea
bar_1 = alt.Chart(tech_d).mark_bar().encode(
    x='count()',
    y='treatment:N')
bar_1


# ## Tip 1: Refactoring code
# 
# At this point we realize that we need to create a reusable function if we want to continue doing multiple similar plots. We need to change the structure of the code maintaining its behavior. This is what we call **'refactoring'**. For instance, if we want to generate the same chart multiple times changing the variable, we can do something like this:

# In[14]:


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


# You may notice that I added a `docstring` documenting both **what goes in**, the `Parameters`, and what **goes out**, the `Return` statement. Adding `docstring` are a way to document the logic of the function, which facilitates future use and debugging.
# 
# Below we use our `plot_cat` function to create a dashboard of bar-charts

# In[15]:


# we can concatenate charts together pretty easily
panel_chart1 = (plot_cat('family_history') | plot_cat('remote_work')) & (plot_cat('care_options')  | plot_cat('anonymity')) 
panel_chart1


# Now let's plot the same variables grouped by treatment (target).

# In[16]:


bar_2= alt.Chart(tech_d).mark_bar().encode(
    x='count()',
    y='family_history',
    color='treatment')
bar_2


# Nice, now we can **refactor** the code as before to make multiple plots.

# In[17]:


def plot_grouped_cat(variable:str)-> 'Chart':
    chart =alt.Chart(tech_d).mark_bar().encode(
        x='count()',
        y=variable,
        color=alt.X('treatment:N'))
    return chart


# In[18]:


panel_chart2 = (plot_grouped_cat('family_history') | plot_grouped_cat('remote_work')) & (plot_grouped_cat('care_options') | plot_grouped_cat('anonymity'))
panel_chart2


# ## Tip 2: saving and time-stamping artifacts
# 
# **Automate the saving of artifacts**, like post-processed data, figures, and others, can save you a lot of typing and time. It also allows to run your code beginning to end with confidence. **Explicitly time-stamping your artifacts** can help you to easily identify different versions of your analysis. Images can add up to large directories, so be mindful before commiting to git/GitHub. One option is to add your results directory to the .gitignore file (after all, your code can reproduce them automatically!).

# In[19]:


date_stamp = date.today().strftime('%Y-%b-%d')
path = '../results'
hist_1.save(f'{path}/hist_1_{date_stamp}.png')
bar_1.save(f'{path}/bar_1_{date_stamp}.png')
bar_2.save(f'{path}/bar_2_{date_stamp}.png')
panel_chart1.save(f'{path}/panel_chart_1_{date_stamp}.png')
panel_chart2.save(f'{path}/panel_chart_2_{date_stamp}.png')


# ## Save Data

# In[20]:


path = '../data'
tech_d.to_csv(f'{path}/mental_health_tech_data_post.csv')


# ## Exporting to python script

# If you like to do your exploratory data analysis in Jupyter, you may consider to save a .py version of your code in case other people don't use Jupyter. It also has the plus of being easy to run in the console (with a few changes, like commenting out magic commands like %watermark)
