import pandas as pd # type: ignore

def integrate_datasets(rainfall_df, crop_df):
    # Simple example join on State and Year
    merged_df = pd.merge(rainfall_df, crop_df, on=['State', 'Year'], how='inner')
    return merged_df
