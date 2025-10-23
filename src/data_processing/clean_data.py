import pandas as pd # type: ignore

def clean_rainfall_data(filepath):
    df = pd.read_csv(filepath)
    # Implement necessary cleaning steps (drop NA, convert types, etc.)
    df = df.dropna()
    df['Year'] = df['Year'].astype(int)
    return df

def clean_crop_data(filepath):
    df = pd.read_csv(filepath)
    # Cleaning steps
    df = df.dropna() ####
    df["Production"] = pd.to_numeric(df["Production"], errors="coerce").fillna(0) # type: ignore
    return df
