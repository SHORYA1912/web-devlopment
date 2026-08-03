import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as s

data = pd.read_csv('gapminder(2007).csv')

data.head()

data.groupby('continent').size().plot(kind='pie', autopct='%.2f')

plt.pie(data.groupby('continent').size(), autopct='%.2f')
labels = ['africa', 'americas', 'asia', 'europe', 'oceania']
labels_distance = 1.15
wedgeprops = {'linewidth': 2, 'edgecolor': 'white'}
plt.show()