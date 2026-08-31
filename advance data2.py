import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

data = pd.read_csv('Titanic Dataset.csv')
data.head(5)

sns.boxplot(data=data, x='Embarked', y='Age' )
plt.show()

plt.scatter( x=data['Fare'], y= data['Survived'])
plt.xlabel("FARE")
plt.ylabel("SURVIVED")
plt.show()

plt.scatter( x=data['Parch'],y=data['Survived'])
plt.xlabel("PARCH")
plt.ylabel("SURVIVED")
plt.show()

plt.scatter(x=data['sibsp'],y=data['Survived'])
plt.xlabel("SIBSP")
plt.ylabel("SURVIVED")
plt.show()

assosiation_categorial = pd.crosstab(data['Gender'],data['Embarked'])
print(assosiation_categorial)
