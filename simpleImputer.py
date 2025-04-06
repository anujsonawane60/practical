import pandas as pd
from sklearn.impute import SimpleImputer

df = pd.read_csv('Iris.csv')

print("Original Dataset Info:")
print(df.info())
print("\nNull values in each column:")
print(df.isnull().sum())

numeric_cols = df.select_dtypes(include=['float64', 'int64']).columns

imputer = SimpleImputer(strategy='mean')

df[numeric_cols] = imputer.fit_transform(df[numeric_cols])

print("\nAfter Imputation:")
print(df.isnull().sum())

# Optional: Save cleaned dataset
# df.to_csv('Iris_cleaned.csv', index=False)
