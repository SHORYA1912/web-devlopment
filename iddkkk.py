import matplotlib.pyplot as plt
import numpy as np
plt.title("SINE AND COSINE GRAPH")
x = np.arange(0, 10, 0.1)
y1 = np.sin(x)
y2 = np.cos(x)
plt.plot(x,y1, 'g', linewidth = 3 , label = "y = sin(x)")
plt.plot(x,y2, 'r', linewidth = 3 , label = "y = cos(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()

plt.title(" SOLVING 2x * 2x +123 and 3x * 3x + 456")
x = np.arange(0, 10, 0.1)
y1 = (2*x**2) + 123
y2 = (3*x**2) + 456
plt.plot(x,y1, 'g', linewidth = 3 , label = "y = 2x^2 + 123")
plt.plot(x,y2, 'r', linewidth = 3 ,label = "y = 3x^2 + 456")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.show()