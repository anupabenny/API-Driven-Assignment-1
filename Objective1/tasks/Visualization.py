import pandas as pd
import matplotlib.pyplot as plt
import io
import logging

df = pd.read_csv('../data/dataset.csv')

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Separate data based on Loan Default categories
default_yes = df[df['Loan Default'] == 'Yes']['Annual Income']
default_no = df[df['Loan Default'] == 'No']['Annual Income']

# Create box plot betweenAnnual Income and Loan Default
plt.figure(figsize=(10, 6))
box = plt.boxplot([default_no, default_yes])

# Manually set x-axis labels
plt.xticks([1, 2], ['No', 'Yes'])  # 1 -> No, 2 -> Yes
plt.title('Box Plot of Annual Income by Loan Default')
plt.xlabel('Loan Default')
plt.ylabel('Annual Income')


# Save the plot to a buffer
buf = io.BytesIO()
plt.savefig(buf, format='jpeg')
buf.seek(0)

# Save the plot as a file
plt.savefig("../output/boxplot1.jpeg")
logger.info("Heat Map saved as 'boxplot1.jpeg'")

# Close the buffer
buf.close()

# Separate data based on Loan Default categories
default_yes = df[df['Loan Default'] == 'Yes']['Credit Score']
default_no = df[df['Loan Default'] == 'No']['Credit Score']

# Create box plot
plt.figure(figsize=(10, 6))
box = plt.boxplot([default_no, default_yes])

# Manually set x-axis labels
plt.xticks([1, 2], ['No', 'Yes'])  # 1 -> No, 2 -> Yes
plt.title('Box Plot of Credit Score by Loan Default')
plt.xlabel('Loan Default')
plt.ylabel('Credit Score')

# Save the plot to a buffer
buf = io.BytesIO()
plt.savefig(buf, format='jpeg')
buf.seek(0)

# Save the plot as a file
plt.savefig("../output/boxplot2.jpeg")
logger.info("Heat Map saved as 'boxplot2.jpeg'")

# Close the buffer
buf.close()

# Create histogram for Loan Term
plt.figure(figsize=(10, 6))
plt.hist(df['Loan Term (months)'], bins=10, edgecolor='black', alpha=0.7)
plt.title('Histogram of Loan Term')
plt.xlabel('Loan Term')
plt.ylabel('Frequency')

# Save the histogram as a file
plt.savefig("../output/histogram_loan_term.jpeg")
logger.info("Histogram saved as 'histogram_loan_term.jpeg'")

# Show both plots
buf.close()

# Create histogram for Annual Income
plt.figure(figsize=(10, 6))
plt.hist(df['Annual Income'], bins=30, edgecolor='black', alpha=0.7)
plt.title('Histogram of Annual Income')
plt.xlabel('Annual Income')
plt.ylabel('Frequency')

# Save the histogram as a file
plt.savefig("../output/histogram_annual_income.jpeg")
logger.info("Histogram saved as 'histogram_annual_income.jpeg'")

# Show both plots
buf.close()
