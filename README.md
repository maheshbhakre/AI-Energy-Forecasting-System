
# ⚡ AI-POWERED ENERGY CONSUMPTION FORECASTING SYSTEM

[![Python](https://img.shields.io/badge/Python-3.12-blue?style=flat-square)] [![ML](https://img.shields.io/badge/ML-MLP%20Regressor-orange?style=flat-square)] [![Status](https://img.shields.io/badge/Status-Completed-green?style=flat-square)]

## ⚡ SYSTEM OVERVIEW
This project is a Machine Learning-based Energy Consumption Forecasting System that predicts electricity usage using historical time-series data. It simulates real-world smart grid systems where AI helps in forecasting future energy demand to improve efficiency, reduce cost, and prevent energy wastage.

## 🔥 WHY THIS PROJECT EXISTS
Traditional energy systems fail to predict demand accurately, leading to power wastage, overproduction of electricity, high operational costs, and poor load balancing. This AI system solves this problem by predicting future energy consumption using machine learning.

## 🏗️ SYSTEM ARCHITECTURE
Data Collection → Data Cleaning → Feature Engineering (Hour, Day) → Train/Test Split → MLP Regressor Model → Model Training → Prediction Engine → Evaluation (MAE, R²) → Visualization Output

## 📊 DATASET OVERVIEW
Time-series energy consumption dataset with columns:
- Datetime
- Energy Consumption (kWh)

Feature Engineering:
- Hour of Day
- Day of Week

## ⚙️ INSTALLATION & SETUP
git clone https://github.com/your-username/AI-Energy-Forecasting-System.git
cd AI-Energy-Forecasting-System
python -m venv venv
venv\Scripts\activate
source venv/bin/activate
pip install -r requirements.txt

## 🚀 USAGE
Run project using:
python main.py

OR use Jupyter Notebook / Colab:
Load dataset → Preprocess data → Train model → Generate predictions → Visualize results

## ⚙️ TECH STACK
Python, Pandas, NumPy, Matplotlib, Scikit-learn, Joblib, MLP Regressor

## 📁 PROJECT STRUCTURE
AI-Energy-Forecasting-System/
├── data/
│   └── energy.csv
├── models/
│   └── energy_forecast_model.pkl
├── outputs/
│   ├── final_energy_forecast.png
│   ├── energy_prediction_graph.png
│   └── graph.png
├── notebooks/
├── src/
├── README.md
└── requirements.txt

## 📈 RESULTS & PERFORMANCE
The model successfully learns energy consumption patterns and captures peak and low usage trends. Evaluation metrics include Mean Absolute Error (MAE) and R² Score.

## 📸 OUTPUT VISUALIZATION
<p align="center">
<img src="outputs/final_energy_forecast.png" width="700"/>
</p>
<p align="center">
<img src="outputs/energy_prediction_graph.png" width="700"/>
</p>
<p align="center">
<img src="outputs/graph.png" width="700"/>
</p>

## 🚀 WHAT I LEARNED
Time-series forecasting, feature engineering, machine learning model training, evaluation techniques, end-to-end ML pipeline development, real-world energy system simulation.

## ⚠️ LIMITATIONS
Only basic time features used (hour, day), no weather data, and model can be improved using deep learning techniques like LSTM.

## 🔮 FUTURE IMPROVEMENTS
Implement LSTM, build Flask API for real-time predictions, create Streamlit dashboard, and use real-world smart grid datasets.

## 🌐 CONNECT WITH ME
GitHub: https://github.com/your-username  
LinkedIn: https://www.linkedin.com/in/your-link  
Instagram: https://www.instagram.com/your-instagram  
Portfolio: https://your-portfolio-link.com  

## 👨‍💻 AUTHOR
Mahesh Bhakre

## ⭐ NOTE
This project demonstrates an end-to-end AI system for energy forecasting used in smart grid and industrial optimization systems.
