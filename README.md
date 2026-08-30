# ☀️ AI & IoT Solar Power Prediction System

An **AI and IoT-based Solar Power Prediction System** designed to monitor solar/environmental parameters and predict solar power generation using **Machine Learning**.

The project combines **ESP32-based IoT monitoring** with a **Random Forest Regression model** to estimate solar power production from parameters such as wind speed, sunshine, air pressure, solar radiation, air temperature, and relative humidity.

## 🚀 Features

* ☀️ Solar power production prediction
* 📡 ESP32-based IoT monitoring
* 🌡️ Temperature monitoring
* 💧 Humidity monitoring
* ⚡ Voltage and current monitoring
* 🔋 Battery monitoring
* 🌞 Solar radiation monitoring
* 🤖 Machine Learning-based prediction
* 🌲 Random Forest Regression model
* 📊 Model performance evaluation using MSE and R²
* 💾 Trained ML model saved using Pickle
* 🚨 Potential for real-time alerts and abnormal-condition detection

## 🛠️ Hardware Components

| Component             | Purpose                             |
| --------------------- | ----------------------------------- |
| ESP32                 | Main IoT controller                 |
| ACS712                | Current measurement                 |
| Voltage Sensor        | Voltage measurement                 |
| DHT22                 | Temperature and humidity monitoring |
| Solar Panel           | Solar power generation              |
| Battery               | Energy storage                      |
| Connecting Components | Circuit implementation              |

## 💻 Software & Technologies

### IoT

* ESP32
* Arduino IDE
* C/C++
* Wi-Fi
* IoT monitoring

### Machine Learning

* Python
* Pandas
* Scikit-learn
* Random Forest Regression
* Pickle
* NumPy

## 📊 Machine Learning Model

The system uses a **Random Forest Regressor** to predict solar power production.

### Input Features

The model uses the following parameters:

```text
WindSpeed
Sunshine
AirPressure
Radiation
AirTemperature
RelativeAirHumidity
```

### Target Variable

```text
SystemProduction
```

In simple terms:

```text
Weather & Solar Parameters
          │
          ▼
   ┌───────────────┐
   │ Random Forest │
   │   Regressor   │
   └───────┬───────┘
           │
           ▼
 Predicted Solar Power
    SystemProduction
```

## 🤖 Machine Learning Workflow

The Python implementation follows these steps:

1. Load the solar power plant dataset.
2. Select relevant environmental and solar features.
3. Separate input features (`X`) and target (`y`).
4. Split the dataset into training and testing sets.
5. Train a Random Forest Regression model.
6. Generate predictions on the test dataset.
7. Evaluate model performance.
8. Save the trained model as `energymodel.pkl`.

### Dataset Split

The current implementation uses:

```text
80% → Training Data
20% → Testing Data
```

with:

```python
random_state = 42
```

## 📈 Model Evaluation

The model is evaluated using two metrics:

### Mean Squared Error (MSE)

MSE measures the average squared difference between the actual and predicted solar power production.

```text
Lower MSE = Better prediction accuracy
```

### R² Score

R² measures how well the model explains the variation in solar power production.

```text
R² closer to 1 = Better model performance
```

The actual MSE and R² values will be displayed when the model is trained.

## 🧠 Random Forest Regression

Random Forest is an ensemble Machine Learning algorithm that combines multiple decision trees to produce a more robust prediction.

Instead of relying on a single decision tree:

```text
              Dataset
                 │
        ┌────────┼────────┐
        ▼        ▼        ▼
      Tree 1   Tree 2   Tree 3   ... Tree N
        │        │        │
        └────────┼────────┘
                 ▼
        Final Prediction
```

This makes Random Forest suitable for capturing complex relationships between environmental conditions and solar power production.

## 📂 Project Structure

```text
AI-IoT-Solar-Power-Prediction/
│
├── solar_power_prediction.py
│
├── energymodel.pkl
│
├── Solar Power Plant Data.csv
│
├── esp32/
│   └── solar_monitoring.ino
│
├── README.md
│
└── .gitignore
```

## ▶️ How to Run the Machine Learning Model

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-IoT-Solar-Power-Prediction
```

### 2. Install the required Python libraries

```bash
pip install pandas scikit-learn
```

### 3. Place the dataset in the project directory

Make sure the dataset is named:

```text
Solar Power Plant Data.csv
```

### 4. Run the Python script

```bash
python solar_power_prediction.py
```

The program will:

* Display the first few rows of the dataset
* Train the Random Forest model
* Calculate MSE
* Calculate R² score
* Save the trained model

The trained model will be saved as:

```text
energymodel.pkl
```

## 📡 IoT System

The ESP32 acts as the IoT controller and collects real-time information from the connected sensors.

```text
              ☀️ Solar Panel
                    │
                    ▼
              ┌───────────┐
              │  Battery  │
              └─────┬─────┘
                    │
          ┌─────────┴─────────┐
          │                   │
          ▼                   ▼
      ACS712             Voltage Sensor
          │                   │
          └─────────┬─────────┘
                    │
                    ▼
                ┌───────┐
                │ ESP32 │
                └───┬───┘
                    │
              ┌─────┴─────┐
              │   DHT22   │
              │Temp/Humid.│
              └───────────┘
                    │
                    ▼
              Wi-Fi / IoT
                    │
                    ▼
          Real-Time Monitoring
```

## 🔋 Battery Monitoring

The IoT portion can monitor:

* Battery voltage
* Charging/discharging current
* Temperature
* Humidity
* Solar generation conditions

The collected parameters can be used to identify battery operating conditions.

Potential battery states include:

```text
Charging
   │
   ├── Normal Charging
   │
   └── Overcharging ⚠️

Discharging
   │
   ├── Normal Discharge
   │
   └── Deep Discharge ⚠️

Idle
   │
   └── Normal

Abnormal
   ├── Overheating ⚠️
   └── Excessive Current ⚠️
```

## 🚨 Alert System

The system can be extended to generate alerts for abnormal operating conditions such as:

* ⚠️ Overcharging
* ⚠️ Deep discharge
* 🌡️ Excessive temperature
* ⚡ Abnormal current
* 🔋 Battery abnormalities

Rather than relying only on fixed thresholds, Machine Learning can be incorporated to identify more complex operating patterns.

## 🔮 Future Improvements

* Integrate ESP32 sensor data directly with the ML model
* Implement real-time solar power prediction
* Add cloud-based data storage
* Add web/mobile dashboard
* Implement battery State of Charge (SOC) prediction
* Implement battery State of Health (SOH) estimation
* Implement Remaining Useful Life (RUL) prediction
* Add anomaly detection
* Add automated notifications
* Store historical sensor data for predictive analytics
* Deploy the ML model as a cloud/API service

## 📌 Key Technologies

```text
ESP32
   +
IoT Sensors
   +
Wi-Fi
   +
Python
   +
Machine Learning
   +
Random Forest
   +
Solar Power Prediction
```

## 👨‍💻 Project Information

**Project:** AI & IoT Solar Power Prediction System

**Domain:** Artificial Intelligence / Machine Learning / IoT / Renewable Energy

**Hardware:** ESP32, ACS712, Voltage Sensor, DHT22

**Programming:** Python, C/C++

**Machine Learning:** Random Forest Regression

**Prediction Target:** Solar Power / System Production

**Communication:** Wi-Fi / IoT

## 📜 License

This project is intended for educational and research purposes. You may modify and extend the implementation for your own projects.
