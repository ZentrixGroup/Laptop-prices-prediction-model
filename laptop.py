import pandas as pd
import numpy as np 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load the dataset
df = pd.read_csv('laptop_prices.csv')

# Feature Engineering: Combine primary and secondary storage into a single feature
df['TotalStorage'] = df['PrimaryStorage'] + df['SecondaryStorage']

# Drop columns that are not needed or have too much noise
silme = ['Product', 'GPU_model', 'SecondaryStorageType', 'CPU_company', 'IPSpanel', 'RetinaDisplay', 'PrimaryStorage', 'SecondaryStorage']
df = df.drop(silme, axis=1)

# Group different Operating System versions into broader categories
os_map = {
    'Windows 10': "Windows",
    'Windows 7': "Windows",
    'Windows 10 S': "Windows",
    'Mac OS X': "Mac",
    'macOS': "Mac",
    'Linux': "Linux",
    'No OS': "No OS",
    'Chrome OS': "Chrome OS",
    'Android': "Android"
}
df['OS'] = df['OS'].replace(os_map)

# Keep only the top 15 most frequent CPU models; set others to NaN
cpu = df['CPU_model'].value_counts().head(15).index
df['CPU_model'] = df['CPU_model'].apply(lambda x: x if x in cpu else np.nan)

# Data Cleaning: Remove rows with missing values and duplicate entries
df = df.dropna()
df = df.drop_duplicates()

# Convert categorical string columns into numerical values
deyisilir = ['Company', 'TypeName', 'Screen', 'Touchscreen', 'PrimaryStorageType', 'GPU_company', 'OS', 'CPU_model']
for x in deyisilir:
    df[x] = pd.factorize(df[x])[0]

# Split the data into features (X) and target variable (y)
x = df.drop('Price_euros', axis=1)
y = df['Price_euros']

# Split the dataset into training (80%) and testing (20%) sets
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)

# Initialize and train the Random Forest Regressor
rf = RandomForestRegressor(random_state=42, n_estimators=150, max_depth=6)
model = rf.fit(X_train, y_train)

# Save the trained model to a file using pickle for future use
pickle.dump(model, open('laptop_price_model.pkl', 'wb'))