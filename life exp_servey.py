import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('gapminder(2007).csv')
data.head()
data.info()
data.isnull().any()

sns.set_style('white')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('dark')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('darkgrid')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('ticks')
sns.countplot(x=data['continent'])
plt.show()

sns.set_style('white')
sns.countplot(x=data['continent'])
sns.despine()
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['continent'], palette='winter')
plt.show()

sns.set_style('whitegrid')
sns.countplot(x=data['continent'],color='purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("paper")
sns.countplot(x=data['continent'],color='purple')
plt.show()


sns.set_style('whitegrid')
sns.set_context("notebook")
sns.countplot(x=data['continent'],color='purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("talk")
sns.countplot(x=data['continent'],color='purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("poster")
sns.countplot(x=data['continent'],color='purple')
plt.show()

sns.set_style('whitegrid')
sns.set_context("poster",font_size=0.8)
sns.countplot(x=data['continent'],color='purple')
plt.show()