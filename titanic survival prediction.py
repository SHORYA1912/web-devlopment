import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statistics

data = pd.read_csv('Titanic Dataset.csv')

data.head()

median_age = np.median(data['Age'])
print("MEDIAN AGE OF THE PASSENGERS IS: ", median_age)

median_fare = np.median(data['Fare'])
print("MEDIAN FARE OF THE PASSENGERS IS: ", median_fare)

mode_age = statistics.mode(data['Age'])
print("MODE AGE OF THE PASSENGERS IS: ", mode_age)

mode_class = statistics.mode(data['Pclass'])
print("MODE CLASS OF THE PASSENGERS IS: ", mode_class)

mode_gender = data['Gender'].value_counts().index[0]
print("MODE GENDER OF THE PASSENGERS IS: ", mode_gender)

