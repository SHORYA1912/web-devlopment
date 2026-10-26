import seaborn  as s
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer

dataset = load_breast_cancer()

s.set_style('dark')
import matplotlib as mpl
mpl.style.use([

'https://gist.githubusercontent.com/BrendanMartin/01e71bb9550774e2ccff3af7574c0020/raw/6fa9681c7d0232d34c9271de9be150e584e606fe/lds_default.mplstyle'

])

print("TARGET VARIABLES:", dataset['target_names'])

(unique, counts) = np.unique(dataset['target'], return_counts=True)
print("UNIQUE variables of target variables",unique)
print("COUNTS of target variables",counts)

s.barplot(x=dataset['target_names'], y=counts)
plt.title("target vaiables count in dataset")
plt.show()