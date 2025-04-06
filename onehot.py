import pandas as pd
from sklearn.preprocessing import LabelEncoder, OneHotEncoder

df = pd.read_csv('Iris.csv')

print("Original Dataset:")
print(df.head())

label_encoder = LabelEncoder()
df['variety_label_encoded'] = label_encoder.fit_transform(df['variety'])

print("\nAfter Label Encoding:")
print(df[['variety', 'variety_label_encoded']].head())

onehot_encoder = OneHotEncoder(sparse_output=False)
encoded_array = onehot_encoder.fit_transform(df[['variety']])

encoded_df = pd.DataFrame(encoded_array, columns=onehot_encoder.get_feature_names_out(['variety']))

df = pd.concat([df, encoded_df], axis=1)

print("\nAfter One-Hot Encoding:")
print(df.head())

# Optional: Save the updated dataset
# df.to_csv('Iris_encoded.csv', index=False)
