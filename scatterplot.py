import pandas as pd
import matplotlib.pyplot as plt

# Load the Iris dataset
df = pd.read_csv('Iris.csv')

# Show column names for verification
print("Available columns:", df.columns)

# Scatter plot: sepal.length vs sepal.width colored by variety
species = df['variety'].unique()
colors = ['red', 'green', 'blue']

plt.figure(figsize=(8, 6))

for sp, color in zip(species, colors):
    subset = df[df['variety'] == sp]
    plt.scatter(subset['sepal.length'], subset['sepal.width'], 
                label=sp, color=color)

# Labels and title
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')
plt.title('Sepal Length vs Sepal Width (Iris Dataset)')
plt.legend()
plt.grid(True)
plt.show()
