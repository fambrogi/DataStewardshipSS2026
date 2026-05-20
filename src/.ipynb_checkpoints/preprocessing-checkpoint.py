import pandas as pd
import numpy as np
import requests

DBREPO_BASE_URL = "https://test.dbrepo.tuwien.ac.at/api"
DATABASE_ID = "bfa4385b-54a9-4ae3-b4f4-cb503d7bb016"

VIEW_ENDPOINT = (
    f"{DBREPO_BASE_URL}/v1/databases/"
    f"{DATABASE_ID}/views/ml_precipitation_features/data"
)


def load_data():

    try:
        response = requests.get(VIEW_ENDPOINT, timeout=30)

        response.raise_for_status()

        data = response.json()

        if "data" not in data:
            raise ValueError("Unexpected API response format")

        df = pd.DataFrame(data["data"])

        return df

    except requests.exceptions.ConnectionError:
        raise RuntimeError(
            "Could not connect to DBRepo API"
        )

    except requests.exceptions.Timeout:
        raise RuntimeError(
            "DBRepo API request timed out"
        )

    except requests.exceptions.HTTPError as e:
        raise RuntimeError(
            f"Unexpected HTTP error: {e}"
        )

    except Exception as e:
        raise RuntimeError(
            f"Unexpected API loading error: {e}"
        )


def clean_dataframe(df):
    df = df.dropna(how="all")
    return df


def feature_engineering(df):

    df = pd.get_dummies(
        df,
        columns=["Ort"],
        drop_first=True
    )

    df["Datum"] = pd.to_datetime(df["Datum"])

    df["date_ordinal"] = (
        df["Datum"]
        .map(pd.Timestamp.toordinal)
    )

    df = df.drop(columns=["Datum"])

    return df


def prepare_features(df):

    return [
        c for c in df.columns
        if c not in [
            "Pb",
            "Cd",
            "date_ordinal"
        ]
    ]