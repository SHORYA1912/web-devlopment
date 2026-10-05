import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

file = "student_data.csv"
file = pd.read_csv(file)

print("FIRST FIVE ROW OF THE DATA:")
print(file.head(5))
plt.show()

print("\nColumn Names :")
print(file.columns)
plt.show()

print("\nNULL VALUSE OF THE DATASET:")
print(file.isnull().sum())
plt.show()

print("\nSHAPE OF THE DATASET:")
print(file.shape)
plt.show()

print("\nDATASET INFORMATION:")
print(file.info())
plt.show()

print("\n DATA AFTER DROPPING THE COLUMN 'island'")
file = file.drop(columns=['island'])
print(file.head(5))
plt.show()

print("\n CHANGING THE DATA 'SPECIES' ")
species = file['Species'].unique()
print(species)
plt.show()

print("\n SHOWING ALL THE CHANGED DATA")
print(file)
plt.show()