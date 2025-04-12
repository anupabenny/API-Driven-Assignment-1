import pandas as pd
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
import io
import logging
import numpy as np
 
df = pd.read_csv("../data/dataset.csv")
print(df)

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

categorical_columns = ['Employment Status', 'Marital Status', 'Loan Type', 'Payment History', 'Loan Default']

label_encoders = {}
for column in categorical_columns:
    le = LabelEncoder()
    df[column] = le.fit_transform(df[column])
    label_encoders[column] = le

# Correlation Matrix - Internally uses Pearson Correlation
corr = df.corr()

# Plotting Heatmap
fig, ax = plt.subplots(figsize=(12, 8))
cax = ax.matshow(corr, cmap='viridis')
fig.colorbar(cax)
ax.set_xticks(np.arange(len(corr.columns)))
ax.set_yticks(np.arange(len(corr.columns)))
ax.set_xticklabels(corr.columns, rotation=45, ha='left', fontsize=10)
ax.set_yticklabels(corr.columns, fontsize=10)
plt.tight_layout()

plt.title("Correlation", fontsize=16, pad=20)

# Save the plot to a buffer
buf = io.BytesIO()
plt.savefig(buf, format='jpeg')
buf.seek(0)

# Save the plot as a file
plt.savefig("../output/HeatMap.jpeg")
logger.info("Heat Map saved as 'HeatMap.jpeg'")

# Close the buffer
buf.close()

