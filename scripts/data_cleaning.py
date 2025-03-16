import pandas as pd
from datetime import datetime
import logging


def clean_import_data(file_path):
    logging.info("Loading dataset...")
    df = pd.read_csv(file_path)

    # Replacing missing values with "Unknown"
    df.fillna("Unknown", inplace=True)

    # Formatting Date Column
    logging.info("Formatting date column...")
    if not pd.api.types.is_datetime64_any_dtype(df['Reg. Date (Day/Mon/Year)']):
        logging.info("Converting 'Reg. Date (Day/Mon/Year)' to datetime...")
        df['Reg. Date (Day/Mon/Year)'] = pd.to_datetime(
            df['Reg. Date (Day/Mon/Year)'],
            infer_datetime_format=True,  # Automatically detect the format
            errors='coerce'  # Coerce invalid dates to NaT
        )
        
    
    # Filter out rows with NaT in 'Reg. Date (Day/Mon/Year)'
    df = df.dropna(subset=['Reg. Date (Day/Mon/Year)'])

    logging.info("Data cleaning completed.")
    return df
