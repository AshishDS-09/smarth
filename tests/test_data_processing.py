from src.data_processing.clean_data import clean_rainfall_data
import pandas as pd # type: ignore

def test_clean_rainfall_data():
    df = clean_rainfall_data("data/raw/test_rainfall.csv")
    assert isinstance(df, pd.DataFrame)
    assert 'Year' in df.columns
