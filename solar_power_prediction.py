import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
import pickle

# Load CSV file
# Replace 'your_file.csv' with the path to your CSV file
data = pd.read_csv('Solar Power Plant Data.csv')

# Display the first few rows to check the structure
print(data.head())

# Select features and target variable
# Replace 'Feature1', 'Feature2', ..., 'Target' with the actual column names
selected_features = ['WindSpeed',	'Sunshine',	'AirPressure',	'Radiation',	'AirTemperature',	'RelativeAirHumidity']  # Replace with your feature column names
target_column = 'SystemProduction'  # Replace with your target column name

X = data[selected_features]
y = data[target_column]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", mse)
print("R-squared:", r2)

# Save the model to a pickle file
with open('energymodel.pkl', 'wb') as file:
    pickle.dump(rf_model, file)

print("Model saved to 'energymodel.pkl'")
