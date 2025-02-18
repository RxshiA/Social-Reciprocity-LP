import os
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score
import pandas as pd

# Get the absolute path to the data directory
current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(os.path.dirname(current_dir))
data_path = os.path.join(project_root, "data", "training_data.csv")

# Load training data
data = pd.read_csv(data_path)

# Features and target
X = data[["accuracy", "sadness", "happiness",
          "engagement", "time_spent", "current_level"]]
y = data["level"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42)

# Train RandomForest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train) 

# Predictions
y_pred = clf.predict(X_test)

# Evaluate the model
print("Classification Report:")
print(classification_report(y_test, y_pred))
print("Accuracy Score:", accuracy_score(y_test, y_pred))

# Feature Importance Analysis
importances = clf.feature_importances_
feature_importances = pd.DataFrame(
    {"Feature": X.columns, "Importance": importances}).sort_values(by="Importance", ascending=False)
print("Feature Importances:")
print(feature_importances)

# Function to Adjust Level
def adjust_level(accuracy, sadness, happiness, engagement, time_spent, current_level):
    features = np.array(
        [[accuracy, sadness, happiness, engagement, time_spent, current_level]])
    predicted_level = clf.predict(features)[0]
    return int(predicted_level)


if __name__ == "__main__":
    # Test the adjust_level function
    print(adjust_level(75, 85, 80, 30, 85, 1))  # Example input
