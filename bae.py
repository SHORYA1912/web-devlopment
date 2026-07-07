import pandas as pd
import matplotlib.pyplot as plt

countries_df = pd.read_csv('Countries Data.csv')
countries = countries_df
countries.head(3)

c_52 = countries.loc[countries['year'] == 1952]
c_52.head()

c_7 = countries.loc[countries['year'] == 2007]
c_7.head()

c_merge = c_52.merge(c_7, left_on='country', right_on='country')
c_merge.head()

c_merge.drop(['year_x', 'year_y'], axis=1)
c_merge.head()

c_merge['population_growth'] = c_merge['population_y'] -c_merge['population_x']
c_merge.head()

31889523 - 8425333

c_merge.shape, type(c_merge)

c_merge = c_merge.sort_values('population_growth', ascending=False).head(10)
c_merge.head(10)

names = ['india','china','united states','pakistan','brazil','bangladesh','mexico',
                'thailand','france','united kingdom']
popgrow = (c_merge['population_growth'] / 10**6 )

plt.figure(figsize=(10, 5))
plt.bar(names, popgrow,width = 0.6) 
plt.xlabel('population growth (in millions)')
plt.ylabel('country')
plt.title('TOP 10 COUNTRIES WITH HIGHEST POPULATION GROWTH BETWEEN 1952 AND 2007')
plt.xticks(rotation=45)

for x , y in zip(names, popgrow):
    label = "{:.2f}".format(y)
    
    plt.annotate(label, (x, y), textcoords="offset points", xytext=(0, 10), ha='center')

plt.show()
