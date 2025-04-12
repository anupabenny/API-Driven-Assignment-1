import pandas as pd
from scipy.stats import pearsonr
import logging
from matplotlib import pyplot as plt
import io
import base64
from sklearn.preprocessing import LabelEncoder

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Import the data
df = pd.read_csv("../data/dataset.csv")
logger.info("Dataset loaded for Pearson correlation.")
df = df.dropna()

le = LabelEncoder()
df['Loan Default'] = le.fit_transform(df['Loan Default'])

list1 = df['Credit Score']
list2 = df['Annual Income']
list3 = df['Loan Amount']
list4 = df['Loan Default']

# Compute Pearson correlation
corr1, _ = pearsonr(list1, list4)
corr2, _ = pearsonr(list2, list4)
corr3, _ = pearsonr(list3, list4)

logger.info(f'Pearson correlation between Credit Score and Loan Default: {corr1:.3f}')
logger.info(f'Pearson correlation between Annual Income and Loan Default: {corr2:.3f}')
logger.info(f'Pearson correlation between Loan Amount and Loan Default: {corr3:.3f}')

plt.figure(figsize=(8, 5))
plt.scatter(df['Credit Score'], df['Loan Default'], alpha=0.6, color='purple')

plt.xlabel('Credit Score')
plt.ylabel('Loan Default (1 = Yes, 0 = No)')
plt.title('Credit Score vs Loan Default')
plt.grid(True)

# Save the plot to a buffer
buf = io.BytesIO()
plt.savefig(buf, format='png')
buf.seek(0)

# Encode the image in base64 and log it
img_base64 = base64.b64encode(buf.read()).decode('utf-8')

# Save the plot as a file
plt.savefig("../output/scatter_plot.png")
logger.info("Scatter plot saved as 'scatter_plot.png'")

# Close the buffer
buf.close()
