import pandas as pd
import logging


def clean_import_data(file_path):
    logging.info("Loading dataset...")
    df = pd.read_csv(file_path)

    # Replacing missing values with "Unknown"
    df.fillna("Unknown", inplace=True)

    # Formatting Date Column
    logging.info("Formatting date column...")
    df['Reg. Date (Day/Mon/Year)'] = pd.to_datetime(df['Reg. Date (Day/Mon/Year)'], errors='coerce')

    # Converting numerical columns to the correct data type
    numeric_columns = ["CIF/FOB Value (ETB)", "FOB (FC)", "Gross Wt. (Kg)", "Net Wt. (Kg)",
                       "Duty tax tobe paid (ETB)", "VAT tobe paid (ETB)", "Total tax tobe paid (ETB)"]
    
    for col in numeric_columns:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    logging.info("Data cleaning completed.")
    return df
