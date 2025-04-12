import pandas as pd
import logging

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

df = pd.read_csv("../data/dataset.csv")

df.head()

# copy the data
df_min_max_scaled = df.copy()
df_min_max_scaled['Credit Score'] = (df_min_max_scaled['Credit Score'] - df_min_max_scaled['Credit Score'].min()) / (df_min_max_scaled['Credit Score'].max() - df_min_max_scaled['Credit Score'].min())	

# view normalized data
lst = []
for val in df_min_max_scaled['Credit Score']:
  lst.append(val) 

formatted_lst = ['%.2f' % elem for elem in lst]

logger.info(formatted_lst[1:10])