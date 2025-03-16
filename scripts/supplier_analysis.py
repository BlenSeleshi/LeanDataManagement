import spacy
import pandas as pd
import logging
from scripts.utils import configure_logging

configure_logging()
nlp = spacy.load("en_core_web_sm")

def identify_suppliers(df):
    logging.info("Starting supplier analysis...")

    suppliers = []
    for desc in df["Commercial / Brand Name"].dropna():
        doc = nlp(desc)
        supplier = [ent.text for ent in doc.ents if ent.label_ == "ORG"]
        suppliers.append(supplier[0] if supplier else "Unknown")

    df["Supplier"] = suppliers
    logging.info("Supplier analysis completed.")
    return df
