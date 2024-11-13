import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([39,173,250,192,102,53]) / np.array([809]*6)
label_x1 = [r'$\leq50$', '50-60', '60-70', '70-80', '80-90', '90-100']

plt.figure(figsize=(8, 4))
plt.stem(x1)
plt.xticks(range(6), label_x1)
plt.xlabel("X")
plt.ylabel(r"PMF@Y=7")
plt.ylim((0, 1))
for i in range(len(x1)):
    plt.text(i, x1[i], f"{x1[i]:.3f}", ha='center', va='bottom')
plt.savefig("x@y=7.png", bbox_inches='tight')

# plt.figure(figsize=(8, 4))
# plt.stem(x2)
# plt.xticks(range(6), label_x2)
# plt.xlabel("X")
# plt.ylabel("PMF@Y=6")
# plt.ylim((0, 1))
# for i in range(len(x2)):
#     plt.text(i, x2[i], f"{x2[i]:.3f}", ha='center', va='bottom')
# plt.savefig("x@y=6.png", bbox_inches='tight')
print(0.214*0.1+0.309*0.2+0.237*0.3+0.126*0.4+0.066*0.5)
plt.show()
