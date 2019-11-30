import pandas as pd
from scipy import stats
import numpy as np

# Test hypothesis that there is a relationship between having a family history of menta health issues and seeking treatment for mental health

# read data in
tech = pd.read_csv('../data/mental_health_tech_data_post_2019-Nov-30.csv')

# create contingency table
crosstab = pd.crosstab(tech['treatment'], tech['family_history'])

# run chi^2 test
Chi_square, p_value, df, exp_freq = stats.chi2_contingency(crosstab)

# print to stdout and text file in ../results
print(f'Pearson Chi-square: {Chi_square}')
print(f'P-value: {p_value}') 
print(f'Degrees of freedom: {df}') 
print('Expected frequencies')
print(pd.DataFrame(exp_freq, index=['No', 'Yes'], columns=['No', 'Yes']))