You have been given a code using linear regression for a classification problem:

import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Load the Wine dataset
wine_data = load_wine()
X = wine_data.data
y = wine_data.target

# Convert data to DataFrame for convenience
df = pd.DataFrame(X, columns=wine_data.feature_names)
df['target'] = y

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create and train the linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict on the test set
y_pred = model.predict(X_test)

# Round the predicted values to the nearest integer
y_pred_rounded = np.round(y_pred).astype(int)

# Evaluate the model accuracy
accuracy = accuracy_score(y_test, y_pred_rounded)
print(f'Accuracy: {accuracy:.2f}')

# Print predicted and actual values for comparison
print("Predicted:", y_pred_rounded)
print("Actual:   ", y_test)

You are required to change the model used here by improving the accuracy as a quality metric. 
This model has accuracy = 0.94.
Write new code for new model, compare accuracy and draw conclusions.
