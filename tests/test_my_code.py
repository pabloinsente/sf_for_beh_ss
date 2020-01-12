from src.stats_helper import critical_value

def test_valid_chi_2():
    # set up
    prob = 0.95
    df = 100
    chi_2_value = 124.342
    expected = 'fail to reject null hypothesis'
    
    # exercise 
    actual = critical_value(prob, df, chi_2_value)
    
    # verify
    assert actual ==  expected
