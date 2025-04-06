import pandas as pd
from sklearn.model_selection import train_test_split

df = pd.read_csv('Iris.csv')

X = df.drop('variety', axis=1)  
y = df['variety']               

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

print(f"Total samples: {len(df)}")
print(f"Training samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

print("\nTraining Features (X_train):")
print(X_train.head())

print("\nTraining Labels (y_train):")
print(y_train.head())
