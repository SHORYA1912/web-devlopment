import seaborn as s
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"import database"

data = pd.read_csv('Titanic Dataset.csv')

data.head()
data.isnull().any()

"NULL VALUES IN THE CABINET"

age_q1 = np.quantile(data['Age'],0.25)
age_q2= np.quantile(data['Age'],0.50)
age_q3 = np.quantile(data['Age'],0.75)

print("QURATILE AGE")
print("Q1 -",age_q1)
print("Q2 -",age_q2)
print("Q3 -",age_q3)

TQR_age = age_q3 - age_q2
print("QUARTILE RANGE :-",TQR_age)

plt.hist(data['Age'])
plt.ylabel("COUNT OF PASENGERS")
plt.xlabel("AGE")
plt.show()
fare_q1 = np.quantile(data['Fare'],0.25)
fare_q2 = np.quantile(data["Fare"],0.50)
fare_q3 = np.quantile(data["Fare"],0.75)

print("QUARTILE FARE")
print("Q1 -",fare_q1)
print("Q2 -",fare_q2)
print("Q3 -",fare_q3)

tqr_fare = fare_q3 - fare_q1

print("FARE QUARTILE RANGE :-",tqr_fare)

bins = np.arange(0,250,20)
plt.hist(data['Fare'],bins = np.arange)
plt.ylabel("COUNT OF PASSENGERS")
plt.xlabel("FARE")
plt.xticks
plt.show()