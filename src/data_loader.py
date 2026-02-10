import pandas as pd


def load_brent_data(filepath: str) -> pd.DataFrame:
    """
    Load Brent oil price data and return a cleaned DataFrame.
    """
    df = pd.read_csv(filepath)
    df["Date"] = pd.to_datetime(df["Date"])
    df = df.sort_values("Date").set_index("Date")
    return df
