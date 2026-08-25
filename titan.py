import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as s

data = pd.read_csv('Titanic Dataset.csv')
data.head(5)

s.countplot(x = "Gender", hue = "Survived", data=data)
plt.show()
s.countplot(x = "Survived",data=data,palette='winter')
plt.show()
s.countplot(x ="Gender", hue = "Survived", data = data, palette ="winter")
plt.show()
s.countplot(x='Embarked',data=data)
plt.show()
s.countplot(x='Embarked',data=data)
plt.xticks
plt.show()


