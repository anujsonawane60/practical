import pandas as pd
from sklearn.preprocessing import StandardScaler

file_path = 'DataPreprocessing.csv' 
df = pd.read_csv(file_path)

print("Original Dataset:")
print(df.head())

numerical_columns = df.select_dtypes(include=['int64', 'float64']).columns

scaler = StandardScaler()
df_scaled = pd.DataFrame(scaler.fit_transform(df[numerical_columns]), columns=numerical_columns)

print("\nDataset after Standardization:")
print(df_scaled.head())
