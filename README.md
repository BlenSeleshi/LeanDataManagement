# **Ethiopian Import Data Analysis - Project**

This project aims to analyze Ethiopian import data (HS Code 3905) for a pilot project targeting a job in the chemical imports, freight forwarding, and logistics business. The project focuses on using AI techniques such as Natural Language Processing (NLP), clustering, and trend analysis to uncover insights related to items, traders, and suppliers.

---

## **Table of Contents**

- [Project Overview](#project-overview)
- [Methodology](#methodology)
- [Data Cleaning](#data-cleaning)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Trader Categorization](#trader-categorization)
- [Supplier Identification](#supplier-identification)
- [Item Categorization](#item-categorization)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

---

## **Project Overview**

This project involves cleaning and analyzing over a million records of import data, which includes a variety of items such as chemicals and raw materials. The objective is to categorize the items, identify suppliers, and predict import purposes using advanced AI methods, ultimately helping to optimize pricing, improve efficiency, and provide actionable insights for the business.

### **Key Features:**

- **Data Cleaning**: Data is cleaned, missing values replaced with 'Unknown', and date fields are properly formatted.
- **Exploratory Data Analysis (EDA)**: Provides summary statistics and trend analysis over time.
- **Trader Categorization**: Categorizes traders by business type using clustering techniques.
- **Supplier Identification**: Identifies suppliers based on the 'Commercial/Brand Name' and 'HS Code'.
- **Item Categorization**: Uses NLP and clustering techniques for item categorization.

---

## **Methodology**

This project uses the following methodology to process the data and extract meaningful insights:

1. **Data Cleaning**:

   - Replace missing values with 'Unknown'.
   - Format date fields properly for analysis.

2. **Exploratory Data Analysis (EDA)**:

   - Analyze trends over time (e.g., imports per year, value of goods).
   - Summary statistics for each field to identify key metrics (e.g., CIF/FOB Value, Quantity).
   - Analyze distributions of key fields (e.g., HS Code, trader names).

3. **Trader Categorization**:

   - Use clustering techniques (e.g., KMeans) to categorize traders into types (e.g., manufacturing, retail).
   - Leverage available features such as trade volume, item types, and business names.

4. **Supplier Identification**:

   - Use NLP (e.g., spaCy) to extract and identify supplier names from the 'Commercial/Brand Name' column.
   - Cross-reference with known supplier lists or other sources for validation.

5. **Item Categorization**:
   - Use TF-IDF vectorization and clustering algorithms to categorize items into predefined categories like 'Polyvinyl Alcohol', 'Chemicals', etc.

---

## **Data Cleaning**

Data cleaning is an essential step to ensure high-quality analysis. The following actions were performed during the data cleaning process:

- Replaced missing values with 'Unknown'.
- Properly formatted the **Reg. Date (Day/Mon/Year)** column into a datetime format.
- Removed any unnecessary whitespace or special characters in the column names.
- Checked for duplicate rows and removed them (if any).

---

## **Exploratory Data Analysis (EDA)**

In this section, we perform EDA on the dataset, which includes:

- **Summary Statistics**: Descriptive statistics such as mean, median, standard deviation, min, and max for numerical columns.
- **Trend Analysis**: Trends in imports over time (e.g., imports per year, values).
- **Item Distribution**: Distribution of item types and HS Codes.
- **Trader Analysis**: Distribution of traders by business type and volume.

---

## **Trader Categorization**

Trader categorization is performed using a **clustering approach** to group traders based on:

- Business volume
- Item categories they import
- Trade patterns over time

### **Steps**:

1. Preprocess features like CIF/FOB values and trader-related information.
2. Use **KMeans** clustering to group traders into types (e.g., manufacturing, retail).
3. Visualize clusters for further analysis.

---

## **Supplier Identification**

Supplier identification is performed using **NLP techniques** (spaCy) to extract potential suppliers from the "Commercial/Brand Name" column:

### **Steps**:

1. Extract and preprocess text data (brand names).
2. Apply **Named Entity Recognition (NER)** to identify and classify suppliers.
3. Validate suppliers by cross-referencing them with a known supplier list or commercial databases.

---

## **Item Categorization**

Item categorization is achieved using **Natural Language Processing (NLP)** and **Clustering**:

### **Steps**:

1. Tokenize and vectorize item descriptions using **TF-IDF**.
2. Apply clustering algorithms (e.g., KMeans) to categorize items into predefined groups.
3. Label items based on their cluster group, such as 'Polyvinyl Alcohol', 'Chemicals', etc.

---

## **Requirements**

- Python 3.x
- Pandas
- NumPy
- Matplotlib
- Seaborn
- spaCy (for NLP tasks)
- Scikit-learn (for clustering and machine learning)
- Jupyter (for notebooks)
- logging

---

## **Installation**

### 1. Clone the repository:

```bash
git clone https://github.com/BlenSeleshi/LeanDataManagement.git
cd ethiopian-import-data-analysis
```

### 2. Create a virtual environment (recommended):

```bash
python -m venv venv
```

### 3. Activate the virtual environment:

For **Windows**:

```bash
venv\Scripts\activate
```

For **macOS/Linux**:

```bash
source venv/bin/activate
```

### 4. Install dependencies:

```bash
pip install -r requirements.txt
```

### 5. Download the spaCy model:

```bash
python -m spacy download en_core_web_sm
```

---

## **Usage**

Once the setup is complete, you can use the Jupyter notebooks to analyze the dataset:

1. **Run the data cleaning and EDA**:

   ```bash
   jupyter notebook
   ```

   Open the **`01_data_cleaning_eda.ipynb`** notebook and follow the steps.

2. **Perform trader categorization**:
   Run the **`02_trader_analysis.ipynb`** notebook.

3. **Run item categorization and supplier identification**:
   Open the **`03_item_and_supplier_analysis.ipynb`** notebook.
