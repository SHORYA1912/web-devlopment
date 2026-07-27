import pandas as pd
import numpy as np
import seaborn as s
import matplotlib.pyplot as plt

data = pd.read_csv('gapminder(2007).csv')

data.head()
data.info()

data.isnull().any()

labels = ["population", "life_exp" ,"gdp_cap"]

for l in labels:
    s.boxplot( y = data[l], palette='winter')
    plt.show()

s.boxplot( y = 'gdp_cap', x= 'continent',data = data ,palette= 'viridis')  
s.boxplot( y = 'life_exp', x= 'continent',data = data ,palette= 'viridis')

s.violinplot(y='gdp_cap', x='continent',data=data, palette='bright')
s.violinplot(y='life_exp', x='continent',data=data, palette='bright')

for l in labels:
    s.kdeplot(data[l])
    plt.show()

for l in labels:
    plt.hist(data[l])
    plt.xlabel(1)
    plt.show()

for l in labels:
  s.distplot(data[l])
  plt.show()
  print("Skewness is :"), data[l].skew()