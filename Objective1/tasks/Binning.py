import pandas as pd
import numpy as np
import logging

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

df = pd.read_csv("../data/dataset.csv")
logger.info("Dataset loaded for binning.")

# Finding max and min values for binning
min_value1 = df['Annual Income'].min()
max_value1 = df['Annual Income'].max()
logger.info(f"Min Income: {min_value1}, Max Income: {max_value1}")

# Finding Bin size for Annual Income
bins1 = np.linspace(min_value1, max_value1, 4)
logger.info(f"Bins for Annual Income: {bins1}")

# Finding max and min values for binning
min_value2 = df['Credit Score'].min()
max_value2 = df['Credit Score'].max()
logger.info(f"Min credit score: {min_value2}, Max credit score: {max_value2}")

# Finding Bin size for Annual Income
bins2 = np.linspace(min_value2, max_value2, 4)
logger.info(f"Bins for Credit Score: {bins2}")

labels1 = ['Low Income', 'Medium Income', 'High Income']
labels2 = ['Low Credit Score', 'Medium Credit Score', 'High Credit Score']

# Equal Width binning
df['bin_width'] = pd.cut(df['Annual Income'], bins=bins1, labels=labels1, include_lowest=True)
logger.info(f"Distance Binning Results:\n{df['bin_width']}")

# Find the length of bins2 array
num_of_bins = len(bins2)

# Equal Frequency binning
df['bin_freq'] = pd.qcut(df['Credit Score'], q=num_of_bins-1, labels=labels2)
logger.info(f"Frequency Binning Results:\n{df['bin_freq']}")
