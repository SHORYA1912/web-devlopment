import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('Countries Data.csv')
countries = countries_df
countries.head(3)

plt.figure(figsize=(10,5))
plt.bar(countries['country'], countries['population'], width = 0.6)
plt.xlabel('Countries')
plt.ylabel('Population')
plt.title('POPULATION OF COUNTRIES')
plt.legend()
plt.show()