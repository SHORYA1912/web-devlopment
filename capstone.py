import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print(sns.get_dataset_names())

df = sns.load_dataset('penguins')

print(df.head(10))
print(df.shape)
print(df.tail())
print(df.isnull().sum())
print(df.describe())
print(df.dtypes)
print(df.info())
print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.show()

df.select_dtypes(include=[np.number]).hist(bins=15, figsize=(15, 10))
plt.show()

df.select_dtypes(include=[np.number]).plot(kind='box', subplots=True, layout=(2, 3), figsize=(15, 10))
plt.show()

print(df.sex.value_counts())
print(df.species.value_counts())
print(df.island.value_counts())

sns.countplot(x = 'sex', data = df)
plt.show()

sns.countplot(x = 'species', data = df)
plt.show()

sns.countplot(x = 'island', data = df)
plt.show()

sns.countplot(x = 'sex',hue= 'species', data = df)
plt.show()

sns.countplot(x = 'island',hue= 'species', data = df)
plt.show()

sns.countplot(data= df, x = 'sex' ,hue= 'species')
plt.show()

sns.countplot(data = df )
plt.show
