import pandas
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv("country_vaccinations.csv")

print(df.info())

print("\n MISSING VALUES IN EACH COLUMN (BEFORE HANDLING)")
print(df.isnull().sum())

plt.figure(figsize=(10, 8))
sns.heatmap(df.isnull(), cbar=True ,cmap= "coolwarm")
plt.title("MISSING VALUE HEAT MAP")
plt.show()

numeric_colounm = df.select_datatypes(include=["number"]).coloumn
df[numeric_colounm] = df[numeric_colounm].filling(df[numeric_colounm].mean())

print("\n MISSING VALUES AFTER HANDLING")
print(df.isnull().sum())