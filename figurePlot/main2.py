import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([86,215,305,351,87,62]) / np.array([1106, 1106, 1106, 1106, 1106, 1106])
label_x1 = [r'$\leq50$', '50-60', '60-70', '70-80', '80-90', '90-100']
x2 = np.array([17, 54, 118, 152, 97, 68]) / np.array([506, 506, 506, 506, 506, 506])
label_x2 = label_x1

plt.figure(figsize=(8, 4))
plt.stem(x1)
plt.xticks(range(6), label_x1)
plt.xlabel("X")
plt.ylabel("PMF@Y=8")
plt.ylim((0, 1))
for i in range(len(x1)):
    plt.text(i, x1[i], f"{x1[i]:.3f}", ha='center', va='bottom')
plt.savefig("x@y=8.png", bbox_inches='tight')

plt.figure(figsize=(8, 4))
plt.stem(x2)
plt.xticks(range(6), label_x2)
plt.xlabel("X")
plt.ylabel("PMF@Y=6")
plt.ylim((0, 1))
for i in range(len(x2)):
    plt.text(i, x2[i], f"{x2[i]:.3f}", ha='center', va='bottom')
plt.savefig("x@y=6.png", bbox_inches='tight')

plt.show()
