import os
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

current_dir = os.path.dirname(os.path.abspath(__file__))
project_root = os.path.dirname(current_dir)
data_path = os.path.join(project_root, "data", "training_data.csv")

# Load data
data = pd.read_csv(data_path)

# Plot distributions
plt.figure(figsize=(12, 8))
for i, column in enumerate(data.columns[:-1], 1):
    plt.subplot(2, 3, i)
    sns.histplot(data[column], kde=True)
    plt.title(f'Distribution of {column}')
plt.tight_layout()
plt.show(block=False)

# Plot correlation matrix
plt.figure(figsize=(10, 8))
correlation_matrix = data.corr()
sns.heatmap(correlation_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
plt.title('Correlation Matrix')
plt.show(block=False)

from sklearn.model_selection import train_test_split

# Features and target
X = data[["accuracy", "sadness", "happiness", "engagement", "time_spent", "current_level"]]
y = data["level"]

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Plot train-test split
plt.figure(figsize=(8, 6))
plt.scatter(X_train['accuracy'], X_train['current_level'], color='blue', label='Train')
plt.scatter(X_test['accuracy'], X_test['current_level'], color='red', label='Test')
plt.xlabel('Accuracy')
plt.ylabel('Current Level')
plt.title('Train-Test Split')
plt.legend()
plt.show(block=False)

from sklearn.ensemble import RandomForestClassifier

# Train RandomForest Classifier
clf = RandomForestClassifier(n_estimators=100, random_state=42)
clf.fit(X_train, y_train)

# Feature Importance
importances = clf.feature_importances_
feature_importances = pd.DataFrame({"Feature": X.columns, "Importance": importances}).sort_values(by="Importance", ascending=False)

# Plot feature importance
plt.figure(figsize=(10, 6))
sns.barplot(x='Importance', y='Feature', data=feature_importances)
plt.title('Feature Importance')
plt.show(block=False)

from sklearn.metrics import classification_report, accuracy_score

# Predictions
y_pred = clf.predict(X_test)

# Classification Report
print("Classification Report:")
print(classification_report(y_test, y_pred))

# Accuracy Score
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy Score:", accuracy)

# Plot accuracy score
plt.figure(figsize=(6, 4))
plt.bar(['Accuracy'], [accuracy], color='green')
plt.ylim(0, 1)
plt.title('Accuracy Score')
plt.show(block=False)

# Ensure all figures are displayed
plt.show()