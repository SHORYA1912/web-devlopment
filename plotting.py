import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as s

data = pd.read_csv("gapminder(2007).csv")

data.head()
data.info()
data.isnull()

s.scatterplot( data = data, x = 'gdp_cap',y = 'life_exp')
plt.show()

s.scatterplot( data=data,x = 'gdp_cap',y = 'life_exp', hue = 'continent')
plt.show()

fig,ax = plt.subplot(figsize=(8,8))

s.scatterplot(data=data, x = 'gdp_cap' ,y = 'life_exp')
plt.show()

s.scatterplot(data = data, x = 'gdp_cap',y = 'life_exp', hue = 'continent')
plt.show()

fig , ax = plt.subplot(figsize=(8,8))

s.scatterplot( data = data, x = 'gdp_cap', y= 'life_exp', size = 'population', alpha = '0.7',
              hue = 'continent', sizes = (20 ,1000), palette= 'BRIGHT')
plt.show()

s.heatmap(data.corr())

s.relplot(data = data,x = 'gdp_cap', y= 'life_exp',col = 'continent', col_wrap= 3, height = 3)

s.pairplot(hue = 'continent', data= data)
