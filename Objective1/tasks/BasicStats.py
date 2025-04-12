import pandas as pd
import logging

# Configure standard logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load the dataset
df = pd.read_csv("../data/dataset.csv")
logger.info("Dataset loaded successfully.")
logger.info(f"DataFrame head:\n{df.head()}")

# Summary statistics
logger.info("Summary Statistics:")
logger.info(f"\n{df.describe(include='all')}")

# Data type information
logger.info("Data Types:")
logger.info(f"\n{df.dtypes}")

# Checking for missing values
logger.info("Missing Values:")
missing_before = df.isnull().sum()
logger.info(missing_before)

# Impute missing data for numeric
columns_to_impute = [
    "Customer ID", "Loan Amount", "Annual Income", "Credit Score", 
    "Employment Status", "Marital Status", "Loan Term (months)", 
    "Number of Dependents", "Previous Defaults", "Loan Type", 
    "Payment History", "Loan Default"
]

for col in columns_to_impute:
    if df[col].dtype in ['float64', 'int64']:
        df[col] = df[col].fillna(df[col].median())
    else:
        df[col] = df[col].fillna(df[col].mode()[0])

missing_after = df.isnull().sum()
missing_check = pd.DataFrame({'Before': missing_before, 'After': missing_after})
print(missing_check[missing_check['Before'] > 0])

# Checking for duplicate values 
logger.info("Number of Duplicate Rows:")
duplicates = df.duplicated().sum()
logger.info(duplicates)

before = df.shape[0]

# Drop duplicates if any
if duplicates > 0:
    df.drop_duplicates(inplace=True)

after = df.shape[0]
logger.info(f"Dropped {before - after} duplicate rows.")