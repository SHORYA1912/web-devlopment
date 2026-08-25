import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as s

data = pd.read_csv('Titanic Dataset.csv')
data.head()
data.info()
data.dtypes

nominal_cat = ['Name','Ticket','Cabin']
ordinal_cat = ['Embarked','Gender']

data['Gender'].value_counts()

gender_catagories = ['Male','Female']

data['Gender']=pd.Categorical(data['Gender'], gender_catagories,ordered = True)

median_index = np.median(data['Gender'].cat.codes)
median_gender = np.median(data['Gender'].cat.codes)
print(median_gender)

data['Embarked'].value_counts()
embark_categories = ['5','c','q']

median_index = np.median(data['Gender'].cat.codes)
median_embark = embark_categories[int(median_index)]
print(median_embark)