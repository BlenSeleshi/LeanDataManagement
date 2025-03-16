from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
import pandas as pd
import logging


def categorize_items(df, num_clusters=5):
    logging.info("Starting item categorization...")

    vectorizer = TfidfVectorizer(stop_words="english")
    X = vectorizer.fit_transform(df["HS Description"].astype(str))

    kmeans = KMeans(n_clusters=num_clusters, random_state=42, n_init=10)
    df["Item Category"] = kmeans.fit_predict(X)

    logging.info("Item categorization completed.")
    return df
