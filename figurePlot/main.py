import matplotlib.pyplot as plt
import numpy as np

marginal_pmf_x = [0.069, 0.111, 0.290, 0.277, 0.185, 0.068]
label_x = [r'$\leq50$', '50-60', '60-70', '70-80', '80-90', '90-100']
marginal_pmf_y = [0.035, 0.176, 0.338, 0.247, 0.155, 0.049]
label_y = [r'$\leq5$', '6', '7', '8', '9', '10']
plt.figure(figsize=(8, 4))
plt.stem(marginal_pmf_x)
plt.xticks(range(6), label_x)
plt.xlabel("X")
plt.ylabel("PMF")
plt.ylim((0, 1))
for i in range(len(marginal_pmf_x)):
    plt.text(i, marginal_pmf_x[i], str(marginal_pmf_x[i]), ha='center', va='bottom')
plt.savefig("marginal_pmf_x.png", bbox_inches='tight')

plt.figure(figsize=(8, 4))
plt.stem(marginal_pmf_y)
plt.xticks(range(6), label_y)
plt.xlabel("Y")
plt.ylabel("PMF")
plt.ylim((0, 1))
for i in range(len(marginal_pmf_y)):
    plt.text(i, marginal_pmf_y[i], str(marginal_pmf_y[i]), ha='center', va='bottom')
plt.savefig("marginal_pmf_y.png", bbox_inches='tight')

plt.show()
