import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as s
import numpy as np
import statistics as st

data=pd.read_csv('IMDB Dataset.csv')
data.head()
data.info()

data.isnull().sum()

plt.hist(data['Runtime'])
plt.xlabel("count of movies")
plt.ylabel("RUNTIME")
plt.show()
plt.hist(data['IBDM_rating'])
plt.xlabel("COUNT OF MOVIE")
plt.ylabel("IMDB RATING")
plt.show()
data['Runtime'].unique()

bins_time = np.arrange(80,230,10)
plt.hist(data['Runtime'],edgecolor = 'black',bins = bins_time, color='g')
plt.ylabel("COUNTS OF MOVIES")
plt.xlabel("RUNTIME")
plt.show()

data['IBDM_rating'].unique()

bins_rating = np.arrange(8,10,0.20)
plt.hist(data['IBDM_rating'],edgecolor = 'black',bins = bins_time, color='g')
plt.ylabel("count of movies")
plt.xlabel("IMDB_RATING")
plt.xticks(bins_rating)