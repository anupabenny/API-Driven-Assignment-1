import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
import logging

# Configure standard Python logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Load dataset
df = pd.read_csv('../data/dataset.csv')

# Encode categorical columns using LabelEncoder
label_encoder = LabelEncoder()

# Loop through the dataset columns and encode only the object (categorical) columns
for column in df.select_dtypes(include=['object']).columns:
    df[column] = label_encoder.fit_transform(df[column])

# Encode the 'Loan Default' target column separately
df['Loan Default Encoded'] = label_encoder.fit_transform(df['Loan Default'])

# Split the data into features and target
X = df.drop(columns=['Loan Default', 'Loan Default Encoded'])  # Drop original and encoded target
y = df['Loan Default Encoded']  # Use the encoded target

# Split the data into train and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train the RandomForestClassifier model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Get feature importances from the RandomForest model
feature_importances = model.feature_importances_

# Create a DataFrame to display the feature importances
feature_importances_df = pd.DataFrame({
    'Feature': X.columns,
    'Importance': feature_importances
}).sort_values(by='Importance', ascending=False)

# Display the top 5 features
logger.info("Top 5 Important Features:")
logger.info(feature_importances_df.head(5))