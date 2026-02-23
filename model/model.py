import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# Simple dataset
data = {
    "experience": [1, 2, 3, 4, 5],
    "salary": [30000, 40000, 50000, 60000, 70000]
}

# Convert to DataFrame
df = pd.DataFrame(data)

# Features and target
X = df[["experience"]]
y = df["salary"]

# Train model
model = LinearRegression()
model.fit(X, y)

# Save model
joblib.dump(model, "model/trained_model.pkl")

print("✅ Model trained and saved successfully!")