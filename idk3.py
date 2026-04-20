import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style= "ticks"

weather_data = pd.read_csv("Weather Dataset - Trial Activity DataSet.csv.csv")
print(weather_data.head())
print(weather_data.info())

sns.barplot(x=weather_data['humidity'], y=weather_data['temperature'], data=weather_data)
plt.title("Humidity vs Temperature")
sns.distplot(weather_data["humidity"])
plt.show()

sns.distplot(weather_data["temperature"])
plt.show()

sns.jointplot(x=weather_data['humidity'], y=weather_data['temperature'], kind="hex")
plt.show()

sns.jointplot(x="weather[`humidity`]", y="weather[`temperature`]", kind = "kde")
plt.show()

sns.pairplot(x = "weather[`humidity`]", y = "weather[`temperature`]", data = weather_data)
plt.show()

sns.stripplot(x="weather[`humidity`]", y="weather[`temperature`]", data=weather_data)
plt.show()

sns.swarmplot(x="weather[`humidity`]", y="weather[`temperature`]", data=weather_data)
plt.show()

sns.stripplpot(x="weather[`humidity`]", y="weather[`temperature`]", data=weather_data, jitter=True)
plt.show()

sns.barplot(x="weather[`humidity`]", y="weather[`temperature`]", hue="weather[`wind_speed`]", data=weather_data)
plt.show()

sns.countplot(x="weather[`humidity`]", hue="weather[`wind_speed`]", data=weather_data)
plt.show()

sns.pointplot(x="weather[`humidity`]", y="weather[`temperature`]", hue="weather[`wind_speed`]", data=weather_data)
plt.show()