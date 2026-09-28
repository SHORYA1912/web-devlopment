import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df = pd.read_csv('USA_Housing (1).csv')

sns.histplot(figsize = (20,20) ,hue= 'AREA INCOME' )
sns.plot(kind = 'plot',subplot = 'true',layout = (5,3), figsize = (12,12))
sns.barplot(x = "AREA INCOME" ,y ="AREA HOUSE AGE", palette= 'SPRING')
df["AREA INCOME"].value_count()
df["AREA HOUSE AGE"].value_count()
sns.countplot( y = 'AREA HOUSE AGE',x = 'AREA INCOME')
sns.countplot
plt.show()