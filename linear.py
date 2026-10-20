import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#matplotlib inline

file = pd.read_csv(r'petrol_consumption.csv')

file.head()
file.describe()

X = file[['Petrol_tax', 'Average_income', 'Paved_Highways', 'Population_Driver_licence(%)']]
y = file['Petrol_Consumption']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)



from sklearn.linear_model import LinearRegression

regressor = LinearRegression()
regressor.fit(x_train, y_train)

coeff_df = pd.DataFrame(x_train.columns, columns=['coefficients'])
y_pred = regressor.predict(x_test)
from sklearn import metrics

df = pd.DataFrame({'Actual': y_test, 'Predicted': y_pred})
print("MEAN SQUARED ERROR:", metrics.mean_squared_error(y_test, y_pred))
print("MEAN ABSOLUTE ERROR:", metrics.mean_absolute_error(y_test, y_pred))
print("ROOT MEAN SQUARED ERROR:", np.sqrt(metrics.mean_squared_error(y_test, y_pred)))