import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Mock data for training
X_train = np.array([
    [70, 50, 80, 1],  # Accuracy, Sadness, Happiness, Current Level
    [50, 60, 70, 1],
    [90, 30, 90, 2],
])
y_train = [2, 1, 3]  # Target levels

# Train a classifier
clf = RandomForestClassifier()
clf.fit(X_train, y_train)


def adjust_level(accuracy, sadness, happiness, current_level):
    features = np.array([[accuracy, sadness, happiness, current_level]])
    predicted_level = clf.predict(features)[0]
    return int(predicted_level)  # Convert numpy.int64 to native Python int


if __name__ == "__main__":
    # Test the adjust_level function
    print(adjust_level(75, 55, 85, 1))  # Example input
