import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

filename = "Titanic Dataset.csv"

titanic = pd.read_csv(filename)

print("\n THE FIRST FIVE ROWS OF THE DATASET:")
titanic.head()
print(titanic.head())

print("\n COLUMN NAME:")
print(titanic.columns)
print(titanic.head())

print("\n SHAPE OF THE DATASET:")
print(titanic.shape)

print("\n  MISSING VALUES:")
print(titanic.isnull().sum())

plt.title("Missing Values in Titanic Dataset")
plt.show()

titanic.drop("cabin", axis = 1 ,inplace = True)

print("DATASET AFTER DROPPING THE CABIN")
print(titanic.head())

plt.title("MISSING VALUES:")
plt.show()

print("\nSEX dummy variable:")
titanic['sex_dummy'] = pd.get_dummies(titanic['sex'], drop_first=True)
print(titanic[['sex', 'sex_dummy']].head())

sex = pd.get_dummies(titanic['sex'], drop_first=True)

print("\nSEX DUMMY VARIABLE:")
print(sex.head(4))

print("EMBARKED DUMMY VARIABLE:")
embarked = pd.get_dummies(titanic['embarked'], drop_first=True)
print(embarked.head(4))

embark = pd.get_dummies(titanic['embarked'], drop_first=True)

print("\nEMBARKED VARIABLE:")
print(embark.head(4))

pclass = pd.get_dummies(titanic['pclass'], drop_first=True)

print("\nPCLASS VARIABLE:")
print(pclass.head(4))

titanic = pd.concat([titanic, sex, embark, pclass], axis=1)

print("\nDATASET AFTER CONCATENATION:")
print(titanic.head())

print("\nFINAL COLUMN NAMES:")
print(titanic.columns)