import matplotlib.pyplot as plt

COMPUTER_PARTS_MADE = [100,  200, 250, 300, 350,  450, 500,525]
COMPUTER_PARTS_BOUGHT = [80,  180, 220, 280, 320, 420, 480,510]
COMPUTER_PARTS_SOLD = [70,  160, 210, 270, 310,  410, 470,480]
COMPUTER_PARTS_DEMAND = [100,200,250,300,350,400,500,550]

type = [COMPUTER_PARTS_MADE, COMPUTER_PARTS_BOUGHT, COMPUTER_PARTS_SOLD, COMPUTER_PARTS_DEMAND]
label = ['MADE', 'BOUGHT', 'SOLD', 'DEMAND']  
bins = [50,100,150,200,250,300,350,400,450,500,550,600]
colors = ['b','g','r','y']
plt.xlabel('COMPUTER PARTS')
plt.ylabel('TOTAL NUMBER OF COMPUTER PARTS')
plt.hist(type, bins=bins, color=colors, label=label, width = 5, orientation='vertical')
plt.legend()
plt.show()