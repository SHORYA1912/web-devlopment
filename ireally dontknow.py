import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn  as s

df= pd.read_csv('Weather Dataset.csv')

df.head()

df_group = df.groupby('month').mean(numeric_only=True)
df_group = df_group.reset_index()

df_group.plot.area(x='month', y='Humidity',alpha = 0.6)

plt.plot(df['Temperature (C)'])
plt.ylabel('Temperature (C)')
plt.xlabel('Reading Number Over The Time')

plt.show()