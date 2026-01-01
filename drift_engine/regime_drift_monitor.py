import pandas as pd

def compute_regime_drift(old_df, new_df):
    old_dist = old_df["Regime"].value_counts(normalize=True).sort_index()
    new_dist = new_df["Regime"].value_counts(normalize=True).sort_index()
    drift = (new_dist - old_dist).fillna(0)
    return drift

def drift_alert(drift, threshold=0.10):
    alerts = drift[abs(drift) > threshold]
    return alerts

