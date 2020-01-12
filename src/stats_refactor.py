import pandas as pd
from scipy import stats
import numpy as np
import stats_helper

# Test hypothesis that there is a relationship between having a family history of menta health issues and seeking treatment for mental health

# load data
tech = stats_helper.read_in('../data/mental_health_tech_data_post.csv')

# create contingency table
crosstab = stats_helper.contigency_table()

# run chi^2 test
Chi_square, p_value, df, exp_freq = stats_helper.run_chi2_test(crosstab)

# compute critical value to interpret test-statistic
prob = 0.95
critical_value_interpretation = stats_helper.critical_value(prob, df, Chi_square)

# print to stdout and text file in ../results
print(f'Pearson Chi-square: {Chi_square}')
print(f'P-value: {p_value}') 
print(f'Degrees of freedom: {df}') 
print(f'Test interpretation: {critical_value_interpretation}')
print('Expected frequencies')
print(pd.DataFrame(exp_freq, index=['No', 'Yes'], columns=['No', 'Yes']))