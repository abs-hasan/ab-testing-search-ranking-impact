"""
Entry-point for running the end-to-end A/B test analysis.
"""
from src.data_processing import load_sessions, load_users, clean_and_merge
from src.stats import run_srm_check, run_conversion_test, run_time_to_booking_test
from src.plotting import plot_conversion_rate
import matplotlib.pyplot as plt


def main():
    # Load data
    sessions = load_sessions('data/sessions.csv')
    users = load_users('data/users.csv')

    # Clean & merge
    df = clean_and_merge(sessions, users)

    # Statistical tests
    chi2_srm, p_srm, srm_passed = run_srm_check(df)
    print(f"SRM check → chi2={chi2_srm:.4f}, p-value={p_srm:.4f}, passed={srm_passed}")

    chi2_conv, p_conv, conv_passed = run_conversion_test(df)
    print(f"Conversion test → chi2={chi2_conv:.4f}, p-value={p_conv:.4f}, significant={conv_passed}")

    stat_time, p_time, time_passed = run_time_to_booking_test(df)
    print(f"Time-to-booking test → stat={stat_time:.4f}, p-value={p_time:.4f}, significant={time_passed}")

    # Plot results
    plot_conversion_rate(df)
    plt.show()


if __name__ == '__main__':
    main()