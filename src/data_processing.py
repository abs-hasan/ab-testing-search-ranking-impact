# src/data_processing.py
"""
Data loading and cleaning utilities for A/B testing project
"""
import pandas as pd

def load_sessions(path: str) -> pd.DataFrame:
    """Load sessions data from CSV"""
    return pd.read_csv(path)


def load_users(path: str) -> pd.DataFrame:
    """Load users data from CSV"""
    return pd.read_csv(path)


def clean_and_merge(sessions: pd.DataFrame, users: pd.DataFrame) -> pd.DataFrame:
    """Merge sessions and users, perform basic cleaning"""
    df = sessions.copy()
    df = df.merge(users, on='user_id', how='left')
    # TODO: add cleaning steps (handle nulls, parse dates)
    return df
