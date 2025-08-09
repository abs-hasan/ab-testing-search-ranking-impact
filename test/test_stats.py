"""
Unit tests for statistical functions
"""
import pandas as pd
import pytest
from src.stats import run_srm_check, run_conversion_test, run_time_to_booking_test

@pytest.fixture
def sample_df():
    data = {
        'experiment_group': ['control']*50 + ['variant']*50,
        'session_id': list(range(100)),
        'conversion': [0]*45 + [1]*5 + [0]*40 + [1]*10,
        'time_to_booking': list(range(50)) + list(range(50))
    }
    return pd.DataFrame(data)


def test_srm_check(sample_df):
    chi2, p, passed = run_srm_check(sample_df)
    assert isinstance(chi2, float)
    assert 0 <= p <= 1
    assert passed is True


def test_conversion_test(sample_df):
    chi2, p, passed = run_conversion_test(sample_df)
    assert isinstance(chi2, float)
    assert 0 <= p <= 1
    assert passed is True


def test_time_to_booking_test(sample_df):
    stat, p, passed = run_time_to_booking_test(sample_df)
    assert isinstance(stat, float)
    assert 0 <= p <= 1
    assert passed is False
