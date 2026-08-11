import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv('Titanic Dataset.csv')
data.head()

mean_age = np.mean(data['Age'])
print("MEAN AGE OF THE PASSENGERS IS: ", mean_age)

mean_fare = np.mean(data['Fare'])
print("MEAN FARE OF THE PASSENGERS IS: ", mean_fare)