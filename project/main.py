import numpy as np
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

def load_and_prepare_data():
    """Load the Wine dataset and prepare it as a DataFrame."""
    wine_data = load_wine()
    X = wine_data.data
    y = wine_data.target
    df = pd.DataFrame(X, columns=wine_data.feature_names)
    df['target'] = y
    return df, X, y

def split_data(X, y, test_size=0.3, random_state=42):
    """Split the data into training and testing sets."""
    return train_test_split(X, y, test_size=test_size, random_state=random_state)

def train_model(X_train, y_train):
    """Train a linear regression model."""
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model

def predict_and_evaluate(model, X_test, y_test):
    """Predict on the test set and evaluate the model accuracy."""
    y_pred = model.predict(X_test)
    y_pred_rounded = np.round(y_pred).astype(int)
    accuracy = accuracy_score(y_test, y_pred_rounded)
    return y_pred_rounded, accuracy

def main():
    # Load and prepare data
    df, X, y = load_and_prepare_data()
    
    # Split the data
    X_train, X_test, y_train, y_test = split_data(X, y)
    
    # Train the model
    model = train_model(X_train, y_train)
    
    # Predict and evaluate
    y_pred_rounded, accuracy = predict_and_evaluate(model, X_test, y_test)
    
    # Print results
    print(f'Accuracy: {accuracy:.2f}')
    print("Predicted:", y_pred_rounded)
    print("Actual:", y_test)

if __name__ == "__main__":
    main()