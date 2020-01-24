import pandas as pd
from scipy import stats
import numpy as np

# Test hypothesis that there is a relationship between having a family history of mental health issues and seeking treatment for mental health

# Step 1: read data in
def read_in(path_df: str):
    df = pd.read_csv(path_df)
    return df
tech = read_in('../data/mental_health_tech_data_post.csv')

# Step 2: create contingency table
def contigency_table(data, var1, var2):
    crosstab = pd.crosstab(data[var1], data[var2])
    return crosstab
crosstab = contigency_table(tech, 'treatment', 'family_history')

# Step 3: run chi^2 test
def run_chi2_test(crosstable):
    Chi_square, p_value, df, exp_freq = stats.chi2_contingency(crosstable)
    return Chi_square, p_value, df, exp_freq

Chi_square, p_value, df, exp_freq = run_chi2_test(crosstab)

# Step 4: compute critical value to interpret test-statistic
def critical_value(prob, df, Chi_square):
    prob = prob
    critical = stats.chi2.ppf(prob, df)
    if abs(Chi_square) >= critical:
        return 'reject null hypothesis'
    else:
        return 'fail to reject null hypothesis'

prob = 0.95
critical_value_interpretation = critical_value(prob, df, Chi_square)

print(f'Pearson Chi-square: {Chi_square}')
print(f'P-value: {np.around(p_value, decimals=10)}') 
print(f'Degrees of freedom: {df}') 
print(f'Test interpretation: {critical_value_interpretation}')
print('Expected frequencies')
print(pd.DataFrame(exp_freq, index=['No', 'Yes'], columns=['No', 'Yes']))