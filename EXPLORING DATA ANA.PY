import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data =pd.read_csv('Titanic Dataset.csv')
data.head(5)
data.info()

sns.countplot(x=data['Gender'], hue=data['Survived'])
plt.show()

sns.countplot(x=data['Pclass'], hue=data['Survived'])
plt.show()

sns.distplot(data['Age'],kde = False,bins=40)
plt.show()

sns.countplot(x=data['Gender'])
plt.show()

sns.countplot(x='Survived',hue='Sibsp',data = data,palette = 'mako')
plt.show()

sns.countplot(x='Survived',hue='Parch',data = data,palette='mako')
plt.show()

sns.distplot(data['Fare'])
plt.show()

sns.countplot(x='Pclass',y='Age',data = data, palette = 'winter')
plt.show()

sns.boxplot(x='Pclass',y='Age',data = data, palette = 'winter')
plt.show()

sns.heatmap(data.corr())
plt.show()