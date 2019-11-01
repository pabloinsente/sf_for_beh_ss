'''
### TIP ###
Always add a brief comment at the top describing the intent of the script
Data analysis script for my awesome project
Created by: Pablo Caceres
Date: Nov-2019
'''

#%%
### TIP ### 
# Dependencies always at the top of the script
# Dependencies may broke.
# You wan't to know if all your dependencies are working fromn the beginning

### TIP ###
# Avoid importing unnecesary dependencies

### TIP ###
# Always make dependencies explicit 
# Don't use 'R profiles' or things that hide your dependencies

import pandas as pd
import numpy as np

# %%

### TIP ###
# Prefer "relative paths" ('../data/survey_results_public.zip') to 
# "full paths" ('~/Desktop/projects/sf_for_beh_ss/data/survey_results_public.zip') 
df = pd.read_csv('../data/survey_results_public.zip', compression='zip')
df.head(2)

# %%
df.dtypes.unique()

# %%
### TIP ###
# Comment "intent" over functionality (unless functionality is unclear)
# Functionality: "print the sum of int64 column types"
# Intent: "verify which data types are we working with for preprocessing"

print(f'int64 count: {df.dtypes.apply(lambda x: x == "int64").sum()}')
print(f'float64 count: {df.dtypes.apply(lambda x: x == "float64").sum()}')
print(f'object count: {df.dtypes.apply(lambda x: x == "O").sum()}')

# %%
# Subsetting data scientist for further analysis 
search = ['data scientist', 'data analyst', 'business analyst', 'machine learning'] # keywords to be searched
filter = list(df.DevType.astype(str)) # list to be filtered
mask = [True if search[0] in x.lower() or search[1] in x.lower() or search[2] in x.lower() or search[3] in x.lower() else False for x in filter] # boolean mask to retain keywords
df_mask = df[mask]
df_ds = df_mask.copy() # we create a new copy to avoid changing the raw data
df_ds.shape

# %%
# Visualize missing values 
nulls = df_ds.isnull().sum().sort_values(ascending=True)
nulls.plot(kind='barh', figsize=(10, 20))

# %%
#df[series].value_counts().apply(lambda x: np.round((x/df[series].notna().sum())*100, decimals=2)).reindex(order).sort_values(ascending = sort).plot(kind=kind, figsize=size, title=title);

df_ds.SOVisitFreq.value_counts().apply(lambda x: np.round((x/df_ds.SOVisitFreq.notna())*100)).plot(kind='barh', title="Stack Overflow Visits Frequency")


# %%


# %%
