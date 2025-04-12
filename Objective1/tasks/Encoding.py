import pandas as pd
import logging
from sklearn.preprocessing import LabelEncoder
 
# 2. Reading the file
df = pd.read_csv("../data/dataset.csv")
print(df)

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

le = LabelEncoder() 

# Apply Label encoding to the nominal field 'Marital Status'
df['Marital Status']=le.fit_transform(df['Marital Status'])
logger.info(df['Marital Status'])

# Apply Label encoding to the nominal field 'Employment Status'
df['Employment Status']=le.fit_transform(df['Employment Status'])
logger.info(df['Employment Status'])

# Apply Label encoding to the nominal field 'Loan Type'
df['Loan Type']=le.fit_transform(df['Loan Type'])
logger.info(df['Loan Type'])

# Apply Label encoding to the nominal field 'Loan Default'
df['Loan Default']=le.fit_transform(df['Loan Default'])
logger.info(df['Loan Default'])

# Apply On-Hot Encoding to the ordinal field 'Payment History'
logger.info(df['Payment History'].value_counts())
one_hot_encoded_data = pd.get_dummies(df, columns = ['Payment History'])
logger.info(one_hot_encoded_data)