import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import statistics

data = pd.read_csv('Titanic Dataset.csv')
data.head()

mean_age = np.mean(data['Age'])
median_age = np.median(data['Age'])
mode_age = statistics.mode(data['Age'])

mean_fare = np.mean(data['Fare'])
median_fare = np.median(data['Fare'])
mode_fare = statistics.mode(data['Fare'])

mean_gender = data['Gender'].value_counts().index[0]
median_gender = data['Gender'].value_counts().index[0]
mode_gender = data['Gender'].value_counts().index[0]

mean_class = data['Pclass'].value_counts().index[0]
median_class = data['Pclass'].value_counts().index[0]
mode_class = data['Pclass'].value_counts().index[0]

print("MEAN AGE OF THE PASSENGERS IS: ", mean_age)
print("MEDIAN AGE OF THE PASSENGERS IS: ", median_age)
print("MODE AGE OF THE PASSENGERS IS: ", mode_age)
print("--------------------------------------------------------------")
print("MEAN FARE OF THE PASSENGERS IS: ", mean_fare)
print("MEDIAN FARE OF THE PASSENGERS IS: ", median_fare)
print("MODE FARE OF THE PASSENGERS IS: ", mode_fare)
print("--------------------------------------------------------------")
print("MEAN GENDER OF THE PASSENGERS IS: ", mean_gender)
print("MEDIAN GENDER OF THE PASSENGERS IS: ", median_gender)
print("MODE GENDER OF THE PASSENGERS IS: ", mode_gender)                                                                
print("--------------------------------------------------------------")
print("MEAN CLASS OF THE PASSENGERS IS: ", mean_class)
print("MEDIAN CLASS OF THE PASSENGERS IS: ", median_class)
print("MODE CLASS OF THE PASSENGERS IS: ", mode_class)