import pandas as pd
import numpy as np
from deltalake import DeltaTable
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow
import mlflow.sklearn

SILVER_SALES_PATH = "fabric_lakehouse/silver/clean_sales"

print("Starting Machine Learning Pipeline...")

# Step 1: Loading Feature Source from Silver Delta Layer

dt_silver = DeltaTable(SILVER_SALES_PATH)
df_silver = dt_silver.to_pandas()

print(f"Loaded {len(df_silver)} transactions from Silver layer.")

#Feature Engineering: Aggregate customer-level behavioral metrics
customer_features = df_silver.groupby("customer_id").agg(
    total_spend = ("amount", "sum"),
    transaction_count = ("transaction_id", "count"),
    avg_order_value = ("amount", "mean")
).reset_index()

# Target Variable Generation (e.g., High-Value Customer classification threshold)
# In production, this would be a true label like Churn or Fraud
customer_features["is_high_value"] = (customer_features["total_spend"] > 150).astype(int)

X = customer_features[["total_spend", "transaction_count", "avg_order_value"]]
y = customer_features["is_high_value"]

X_train, X_test, y_train, y_test =  train_test_split(X, y, test_size=0.2, random_state=42)

# Step 2: Initializing MLflow Tracking (Mirroring Fabric ML Experience)
mlflow.set_experiment("fabric_customer_segmentation")

print("\n--- Training Model & Logging Experiment with MLflow ---")

with mlflow.start_run(run_name="RandomForest_v1"):
    #Hyperparameters
    n_estimates = 100
    max_depth = 5

    #Model Training
    model = RandomForestClassifier(n_estimators=n_estimates, max_depth=max_depth, random_state=42)
    model.fit(X_train, y_train)

    #Predictions & Evalutation
    y_pred = model.predict(X_test)

    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred, zero_division=0)
    rec = recall_score(y_test, y_pred, zero_division=0)
    f1 = f1_score(y_test, y_pred, zero_division=0)

    # Step 3: Explicit MLflow Parameter & Metric Logging
    mlflow.log_param("n_estimators", n_estimates)
    mlflow.log_param("max_depth", max_depth)
    mlflow.log_param("data_source_version", dt_silver.version())

    mlflow.log_metric("accuracy", acc)
    mlflow.log_metric("precision", prec)
    mlflow.log_metric("recall", rec)
    mlflow.log_metric("f1_score", f1)

    # Log Trained Model Artifact
    mlflow.sklearn.log_model(model, "random_forest_model")

    print(f"Logged Run Parameters: n_estimators={n_estimates}, max_depth={max_depth}")
    print(f"Logged Silver Data Version Used: Version {dt_silver.version()}")
    print(f"Metrics -> Accuracy: {acc:.2f} | Precision: {prec:.2f} | F1: {f1:.2f}")

print("\nMachine Learning experiment logged successfully!")

