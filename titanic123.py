import seaborn as s
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

"import database"

data = pd.read_csv('Titanic Dataset.csv')

"CHECK NULL VALUES"

data.head()
data.isnull().any()

"BOXPLOT AGE AND PCLASS"

plt.boxplot(data['Pclass'])
plt.title("PASSENGER CLASS DISRTIBUTION")
plt.show()

plt.boxplot(data['Age'])
plt.title("AGE DISTRIBUTION")
plt.show()