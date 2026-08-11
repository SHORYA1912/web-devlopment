import seaborn as s
import matplotlib.pyplot as plt
import numpy as n
import pandas as p

data =p.read_csv('Titanic Dataset.csv')

data.dtypes
print(data.dtypes)

data.isnull().sum()