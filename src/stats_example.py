import pandas as pd
from scipy import stats
import numpy as np

# Test hypothesis that there is a relationship between having a family history of menta health issues and seeking treatment for mental health

# read data in
def read_in(path_df: str):
    df = pd.read_csv(path_df)
    return df
tech = read_in('../data/mental_health_tech_data_post.csv')

# create contingency table
def contigency_table():
    crosstab = pd.crosstab(tech['treatment'], tech['family_history'])
    return crosstab
crosstab =  contigency_table()

# run chi^2 test
def run_chi2_test(crosstable):
    Chi_square, p_value, df, exp_freq = stats.chi2_contingency(crosstab)
    return Chi_square, p_value, df, exp_freq

Chi_square, p_value, df, exp_freq = run_chi2_test(crosstab)

# compute critical value to interpret test-statistic

def critical_value(prob, df, Chi_square):
    prob = prob
    critical = stats.chi2.ppf(prob, df)
    if abs(Chi_square) >= critical:
        return 'reject null hypothesis'
    else:
        return 'fail to reject null hypothesis'

prob = 0.95
critical_value_interpretation =  critical_value(prob, df, Chi_square)

# print to stdout and text file in ../results
print(f'Pearson Chi-square: {Chi_square}')
print(f'P-value: {p_value}') 
print(f'Degrees of freedom: {df}') 
print(f'Test interpretation: {critical_value_interpretation}')
print('Expected frequencies')
print(pd.DataFrame(exp_freq, index=['No', 'Yes'], columns=['No', 'Yes']))