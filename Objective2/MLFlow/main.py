import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, precision_score, recall_score, f1_score, confusion_matrix
import mlflow
import mlflow.sklearn
import psutil
import time

# Set MLflow tracking URI
mlflow.set_tracking_uri("http://localhost:5000")

# Data preprocessing
def preprocess_data(data):
    data = pd.get_dummies(data, columns=['department'], drop_first=True)
    X = data.drop(columns=['job_involvement', 'satisfaction_class'])
    y = data['satisfaction_class']
    return X, y

# Train the model
def train_model(X_train, y_train, max_depth=3, use_logistic_regression=False):
    if use_logistic_regression:
        clf = LogisticRegression(max_iter=1000)
    else:
        clf = DecisionTreeClassifier(max_depth=max_depth, random_state=42)
    clf.fit(X_train, y_train)
    return clf

# Evaluate the model
def evaluate_model(model, X_test, y_test):
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred, average='macro')
    recall = recall_score(y_test, y_pred, average='macro')
    f1 = f1_score(y_test, y_pred, average='macro')
    confusion = confusion_matrix(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}\nF1-score: {f1:.2f}")
    print("Classification Report:\n", classification_report(y_test, y_pred))
    return accuracy, precision, recall, f1, confusion

# Log to MLflow
def log_to_mlflow(model, model_name, metrics, confusion, training_time, use_logistic_regression):
    with mlflow.start_run(run_name=model_name):
        mlflow.log_param("model_type", model_name)
        if not use_logistic_regression:
            mlflow.log_param("max_depth", model.max_depth)

        mlflow.log_metrics({
            "accuracy": metrics[0],
            "precision": metrics[1],
            "recall": metrics[2],
            "f1_score": metrics[3],
            "true_positive": confusion[1][1],
            "false_positive": confusion[0][1],
            "true_negative": confusion[0][0],
            "false_negative": confusion[1][0],
            "system_model_training": training_time,
            "system_cpu_usage": psutil.cpu_percent(interval=1),
            "system_memory_usage": psutil.virtual_memory().percent,
        })

        mlflow.sklearn.log_model(model, "model")

# Main function
def main():
    data = pd.read_csv("employee_satisfaction_data.csv")
    X, y = preprocess_data(data)
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

    models = [
        ("DecisionTree", False),
        ("LogisticRegression", True)
    ]

    results = []

    for name, is_logreg in models:
        start = time.time()
        model = train_model(X_train, y_train, max_depth=3, use_logistic_regression=is_logreg)
        end = time.time()
        train_time = end - start

        metrics = evaluate_model(model, X_test, y_test)
        log_to_mlflow(model, name, metrics, metrics[4], train_time, is_logreg)
        results.append((name, metrics[3]))

    best_model = max(results, key=lambda x: x[1])
    print(f"\nBest Model: {best_model[0]} with F1-score: {best_model[1]:.2f}")

if __name__ == "__main__":
    main()