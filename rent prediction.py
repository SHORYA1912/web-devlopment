import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

# Read the CSV file

HouseDF = pd.read_csv("USA_Housing.csv")

# Display first 5 rows

print(HouseDF.head())

# Display dataset information

print(HouseDF.info())

# Display column names

print(HouseDF.columns)

# Pairplot

sns.pairplot(HouseDF)

plt.show()

# Select only numeric columns

numeric_df = HouseDF.select_dtypes(include=['number'])

# Correlation matrix

corr = numeric_df.corr()

# Heatmap

plt.figure(figsize=(10, 8))

sns.heatmap(corr, annot=True, cmap="coolwarm", linewidths=0.5)

plt.title("Correlation Heatmap")

plt.show()