import pandas as pd
from scipy import stats
import numpy as np

# read data in
def read_in(path_df: str):
    df = pd.read_csv(path_df)
    return df

# create contingency table
def contigency_table(data, var1, var2):
    crosstab = pd.crosstab(data[var1], data[var2])
    return crosstab

# run chi^2 test
def run_chi2_test(crosstable):
    Chi_square, p_value, df, exp_freq = stats.chi2_contingency(crosstable)
    return Chi_square, p_value, df, exp_freq

# compute critical value to interpret test-statistic
def critical_value(prob, df, Chi_square):
    prob = prob
    critical = stats.chi2.ppf(prob, df)
    if abs(Chi_square) >= critical:
        return 'reject null hypothesis'
    else:
        return 'fail to reject null hypothesis'
