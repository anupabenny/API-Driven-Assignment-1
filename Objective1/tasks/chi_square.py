import pandas as pd
import scipy.stats as stats
import logging

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load the dataset
df = pd.read_csv("../data/dataset.csv")
logger.info("Dataset loaded for chi-square Test")

# Create a contingency table for Employment Status and Loan Default
new = pd.crosstab(df["Employment Status"], df["Loan Default"])

# Create a contingency table for Marital Status and Loan Default
new1 = pd.crosstab(df["Marital Status"], df["Loan Default"])

# Perform the Chi-Square test
chi2, p1, dof1, expected1 = stats.chi2_contingency(new)
chi21, p2, dof2, expected2 = stats.chi2_contingency(new1)

# Print results
logger.info(f"Chi-Square Statistic: {chi2}")
logger.info(f"Degrees of Freedom: {dof1}")
logger.info(f"P-value:, {p1}")

# Interpretation
alpha = 0.05
if p1 <= alpha:
	logger.info("Dependent (reject H0)")
else:
	logger.info("Independent (H0 holds true)")


# Print results
logger.info(f"Chi-Square Statistic: {chi21}")
logger.info(f"Degrees of Freedom: {dof2}")
logger.info(f"P-value:, {p2}")

if p2 <= alpha:
	logger.info("Dependent (reject H0)")
else:
	logger.info("Independent (H0 holds true)")