import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import warnings as w

w.filterwarnings("ignore")
df = pd.read_csv("heart.csv")
df.head()
df.shape
df.columns
df.describe()
df.isnull().sum()
print(df.info())
df.hist(figsize=(12, 10))
df.plot(kind='box', subplots=True, layout=(5, 3), figsize=(12, 12))
plt.show()
sns.barplot(x='sex', y='chol', hue='target', palette='spring', data=df)
df['sex'].value_count()
df['target'].value_count()
df['thal'].value_count()
plt.figure(figsize=(20,10))
sns.heatmap(df.corr(), annot= True ,cmap = 'terrain' )
sns.countplot(x ='sex',data = df,palette = 'husl',hue = 'target' )
sns.countplot(x ='target', palette='BUGn', data = df )
sns.countplot(x = 'ca',hue = 'target',data = df)
