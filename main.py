import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPRegressor
from sklearn.metrics import mean_absolute_error, r2_score

# -----------------------------
# 1. LOAD DATASET
# -----------------------------
data = pd.read_csv("data/energy.csv", parse_dates=["Datetime"])
data.set_index("Datetime", inplace=True)

# -----------------------------
# 2. RESAMPLE & CLEAN
# -----------------------------
data = data.resample("H").mean()
data = data.fillna(method="ffill")

# -----------------------------
# 3. FEATURE ENGINEERING
# -----------------------------
data["hour"] = data.index.hour
data["day"] = data.index.dayofweek

X = data[["hour", "day"]]
y = data["Energy"]

# -----------------------------
# 4. TRAIN TEST SPLIT
# -----------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# -----------------------------
# 5. MODEL TRAINING
# -----------------------------
model = MLPRegressor(hidden_layer_sizes=(64, 64), max_iter=500)
model.fit(X_train, y_train)

# -----------------------------
# 6. PREDICTION
# -----------------------------
predictions = model.predict(X_test)

# -----------------------------
# 7. EVALUATION
# -----------------------------
mae = mean_absolute_error(y_test, predictions)
r2 = r2_score(y_test, predictions)

print("\nMODEL PERFORMANCE")
print("MAE:", mae)
print("R2 Score:", r2)

# -----------------------------
# 8. SAVE MODEL
# -----------------------------
joblib.dump(model, "models/energy_model.pkl")
print("\nModel saved as models/energy_model.pkl")

# -----------------------------
# 9. VISUALIZATION
# -----------------------------
plt.figure(figsize=(10,5))
plt.plot(y_test.values[:100], label="Actual")
plt.plot(predictions[:100], label="Predicted")
plt.legend()
plt.title("Energy Consumption Prediction vs Actual")
plt.show()

# -----------------------------
# 10. SIMPLE SIMULATION INPUT
# -----------------------------
hour = 14
day = 2

sample = np.array([[hour, day]])
result = model.predict(sample)

print("\nSAMPLE PREDICTION")
print("Hour:", hour, "Day:", day)
print("Predicted Energy:", result[0])