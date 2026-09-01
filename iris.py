import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


data = pd.read_csv('Iris Dataset.csv')

data.head(5)
data.info()

data.describe()

labels = ['id','sepal_length','sepal_width','petal_length','petal_width']
for labels in labels:
        print("DISTRIBUTION OF",labels)
        sns.distplot(data[labels])
        plt.show()
        

sns.heatmap(data.corr())

labels = ['id','sepal_length','sepal_width','petal_length','petal_width']
for labels in labels:
        print("DISTRIBUTION OF",labels)
        sns.countplot(data[labels])
        plt.show()

labels = ['id','sepal_length','sepal_width','petal_length','petal_width']
for labels in labels:
        print("DISTRIBUTION OF",labels)
        print("skewness -",data[labels].skew())

