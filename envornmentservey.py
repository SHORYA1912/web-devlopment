import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as s

data = pd.read_csv('FuelConsumption.csv')

data.head()
data.isnull().any()

df_grouped = data.groupby(data['VEHICLECLASS']).mean(numeric_only=True)

df_grouped.head()

x = np.arange(0,len(df_grouped.index))
x = np.arange(0, len(df_grouped.index))

plt.bar(x, df_grouped['FUELCONSUMPTION_CITY'], bottom=df_grouped['FUELCONSUMPTION_HWY'], 
        color = '#1D2F6F')

plt.bar(x, df_grouped['FUELCONSUMPTION_HWY'], color = '#8390FA')

plt.bar(x, df_grouped['FUELCONSUMPTION_COMB'], bottom=df_grouped['FUELCONSUMPTION_COMB'], 
        color = '#6EAF46')

plt.ylabel('Fuel Consumption')

plt.xticks(x, df_grouped.index, rotation=90)

plt.legend(['City','Highway','Combined'])

plt.title('Average Fuel Consumption for Different Vehicle Type')

plt.show()