"""
Plotting utilities for A/B testing results
"""
import matplotlib.pyplot as plt
import seaborn as sns

def plot_conversion_rate(df, group_col='experiment_group', outcome_col='conversion'):
    rates = df.groupby(group_col)[outcome_col].mean().reset_index()
    sns.barplot(x=group_col, y=outcome_col, data=rates)
    plt.title('Conversion Rate by Group')
    plt.ylabel('Conversion Rate')
    plt.xlabel('Experiment Group')
