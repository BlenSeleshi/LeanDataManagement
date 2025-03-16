from sklearn.cluster import KMeans
import pandas as pd
import logging


def categorize_traders(df, num_clusters=5):
    logging.info("Starting trader categorization...")

    trader_data = df.groupby("Trader")["CIF/FOB Value (ETB)"].sum().reset_index()
    trader_data["Trader Category"] = KMeans(n_clusters=num_clusters, random_state=42, n_init=10).fit_predict(trader_data[["CIF/FOB Value (ETB)"]])

    logging.info("Trader categorization completed.")
    return trader_data
