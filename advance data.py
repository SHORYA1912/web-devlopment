import numpy as np
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt

data = pd.read_csv('Titanic Dataset.csv')
data.head(5)

mini_age = data['Age'].min()
print("MINIMUM AGE:",mini_age)

max_age = data['Age'].max()
print("MAXIMUM AGE",max_age)

bins = [0,15,30,45,60,75]

data['Binned_age'] = pd.cut(data['Age'],bins)
age_label = ['young','young-adult','middle-age','middle-older-age','senior']

data['Binned_age'] = pd.cut(data['Age'],bins,labels = age_label)

data['Binned_age'].value_counts().plot(kind = 'bar')

plt.title("DANCE CLASS AGE DISTRIBUTION")
plt.xlabel("AGE")
plt.ylabel("COUNT")

"CONCLUSION"
"check distribution and skewness of all features"

labels = ['PassengerId','Survived','Pclass','Name','Age','SibSp','Parch','Ticket','Fare']
for labels in labels:
    print("DISTRIBUTION OF",labels)
    sns.distplot(data[labels])
    plt.show()
    print("skewness -",data[labels].skew())

"conclusion"
"features :- sibsp,parch and skewerness"

data['log_sibsp'] = np.log(data['sibsp'])
data['log_parch'] = np.log(data['parch'])
data['log_fare'] = np.log(data['fare'])

