import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import logging


def perform_eda(df):
    logging.info("Starting EDA...")

    # Summary statistics
    logging.info("Generating summary statistics...")
    summary = df.describe()

    # # Import trend over time
    # df['Year'] = df['Reg. Date (Day/Mon/Year)'].dt.year
    # yearly_imports = df.groupby('Year')['CIF/FOB Value (ETB)'].sum()

    # plt.figure(figsize=(10,5))
    # sns.lineplot(x=yearly_imports.index, y=yearly_imports.values, marker="o")
    # plt.title("Yearly Import Value Trend")
    # plt.xlabel("Year")
    # plt.ylabel("Total Import Value (ETB)")
    # plt.show()

    # Top imported items
    top_items = df['HS Description'].value_counts().head(10)
    plt.figure(figsize=(12,6))
    sns.barplot(x=top_items.index, y=top_items.values)
    plt.xticks(rotation=90)
    plt.title("Top 10 Imported Items")
    plt.show()

    logging.info("EDA completed.")
    return summary
