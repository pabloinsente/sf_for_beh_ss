from src.stats_helper import critical_value

def test_valid_chi_2():
    # step 1: set up
    prob = 0.95
    df = 100
    chi_2_value = 124.342
    expected = 'fail to reject null hypothesis'
    
    # step 2: exercise 
    actual = critical_value(prob, df, chi_2_value)
    
    # step 3: verify
    assert actual ==  expected
