import pandas as pd
import numpy as np

def load_data(path):
    return pd.read_csv(path)

def apply_quality_flags(df):
    for col in df.columns:
        if "_flag" in col:
            base = col.replace("_flag", "")
            df.loc[df[col] != 1, base] = np.nan
    return df

def clean_dataframe(df):
    df = apply_quality_flags(df)
    df = df[[col for col in df.columns if "_flag" not in col]]
    df = df.dropna(how="all")
    return df

def feature_engineering(df):
    df = pd.get_dummies(df, columns=["Ort"], drop_first=True)
    df["Datum"] = pd.to_datetime(df["Datum"])
    df["date_ordinal"] = df["Datum"].map(pd.Timestamp.toordinal)
    df = df.drop(columns=["Datum"])
    return df

def prepare_features(df):
    return [c for c in df.columns if c not in ["Pb", "Cd","date_ordinal"]]
