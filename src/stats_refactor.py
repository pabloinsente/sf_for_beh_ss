import pandas as pd
from scipy import stats
import numpy as np
import stats_helper as sh

# Test hypothesis that there is a relationship between having a family history of mental health issues and seeking treatment for mental health

# Step 1: read data in
tech = sh.read_in('../data/mental_health_tech_data_post.csv')

# Step 2: create contingency table
crosstab = sh.contigency_table(tech, 'treatment', 'family_history')

# Step 3: run chi^2 test
Chi_square, p_value, df, exp_freq = sh.run_chi2_test(crosstab)

# Step 4: compute critical value to interpret test-statistic
prob = 0.95
critical_value_interpretation = sh.critical_value(prob, df, Chi_square)

# Step 5: print to stdout
print(f'Pearson Chi-square: {Chi_square}')
print(f'P-value: {p_value}') 
print(f'Degrees of freedom: {df}') 
print(f'Test interpretation: {critical_value_interpretation}')
print('Expected frequencies')
print(pd.DataFrame(exp_freq, index=['No', 'Yes'], columns=['No', 'Yes']))