import matplotlib.pyplot as plt

BLOOD_SUGAR_MEN= [113,85,90,150,149,88,93,120,130,140]
BLOOD_SUGAR_WOMEN = [67,89,98,120,133,150,130,75,80,110]

type = [BLOOD_SUGAR_MEN,BLOOD_SUGAR_WOMEN]

colors = ['g','r']
labels = ['MEN','WOMEN']
bins = [80,100,125,140]
plt.xlabel ( 'BLOOD SUGAR LEVELS')
plt.ylabel  ('TOTAL NUMBER OF PATIENTS')

plt.hist(type, bins=bins, color=colors, label=labels ,width = 0.9 ,orientation='horizontal')
plt.title('BLOOD SUGAR LEVELS OF MEN AND WOMEN')
plt.legend()
plt.show()