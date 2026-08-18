import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as s
import statistics as st

data = pd.read_csv('Weather Dataset.csv')
data.head()
data.info()

data.isnull().any()

mean_temp = np.mean(data['Temperature (C)'])
print("TEMPERATURE :",mean_temp)

var_temp = np.var(data['Temperature (C)'])
print("VARIATION OF TEMPERATURE :",var_temp)

std_temp = np.std(data['Temperature (C)'])
print("STANDARD DEVIATION IS :",std_temp)

for i in range (1,13):
    month = data.loc[data["month"] == i]["Temperature (C)"]
    print("FOR MONTH", str(i))
    print("MEAN TEMPERATURE IS:"+ str( np.mean(month)))
    print("STANDARD DEVIATION IS:"+ str( np.mean(month))+ "/n")