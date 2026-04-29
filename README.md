# 💻 Laptop Price Predictor

This repository contains a machine learning project designed to estimate laptop prices based on their technical specifications. Using a **Random Forest Regressor**, the model analyzes features like CPU, RAM, OS, and Storage to provide price insights.

## 📌 Project Features
* **Data Preprocessing:** Cleaning duplicates and handling missing values.
* **Feature Engineering:** * Merged Primary and Secondary storage into a single `TotalStorage` feature.
    * Simplified Operating System categories (e.g., grouping all Windows versions).
    * Filtered top 15 CPU models to maintain model focus and accuracy.
* **Data Encoding:** Categorical features are transformed using Label Factorization.
* **Model:** Random Forest Regressor ($n=150$, $depth=6$).
* **Persistence:** The trained model is exported as a `.pkl` file for easy integration.

## 🛠️ Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/ZentrixGroup/laptop-price-predictor.git](https://github.com/your-username/laptop-price-predictor.git)
    ```

2.  **Install required libraries:**
    ```bash
    pip install pandas numpy scikit-learn
    ```

3.  **Data:**
    Make sure the `laptop_prices.csv` file is in the root directory.

## 🚀 How to Run
Simply execute the Python script to train the model and save the serialized file:
```bash
python training_script.py
