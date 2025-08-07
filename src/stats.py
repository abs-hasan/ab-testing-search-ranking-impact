"""
Statistical test functions for A/B analysis
"""
import pandas as pd
from scipy.stats import chi2_contingency, mannwhitneyu


def run_srm_check(df: pd.DataFrame, group_col: str = 'experiment_group', alpha: float = 0.01):
    table = pd.crosstab(df[group_col], df['session_id'].notnull())
    chi2, p, _, _ = chi2_contingency(table)
    return chi2, p, (p >= alpha)


def run_conversion_test(df: pd.DataFrame, group_col: str = 'experiment_group', outcome_col: str = 'conversion', alpha: float = 0.1):
    table = pd.crosstab(df[group_col], df[outcome_col])
    chi2, p, _, _ = chi2_contingency(table)
    return chi2, p, (p < alpha)


def run_time_to_booking_test(df: pd.DataFrame, group_col: str = 'experiment_group', time_col: str = 'time_to_booking', alpha: float = 0.1):
    control = df[df[group_col]=='control'][time_col].dropna()
    variant = df[df[group_col]=='variant'][time_col].dropna()
    stat, p = mannwhitneyu(control, variant, alternative='two-sided')
    return stat, p, (p < alpha)
