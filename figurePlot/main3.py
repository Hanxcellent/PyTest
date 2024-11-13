import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([6, 17, 62, 53, 68, 21]) / np.array([227]*6)
label_x1 = [r'$\leq5$', '6', '7', '8', '9', '10']

plt.figure(figsize=(8, 4))
plt.stem(x1)
plt.xticks(range(6), label_x1)
plt.xlabel("Y")
plt.ylabel(r"PMF@X$\leq50$")
plt.ylim((0, 1))
for i in range(len(x1)):
    plt.text(i, x1[i], f"{x1[i]:.3f}", ha='center', va='bottom')
plt.savefig("y@xleq50.png", bbox_inches='tight')

# plt.figure(figsize=(8, 4))
# plt.stem(x2)
# plt.xticks(range(6), label_x2)
# plt.xlabel("X")
# plt.ylabel("PMF@Y=6")
# plt.ylim((0, 1))
# for i in range(len(x2)):
#     plt.text(i, x2[i], f"{x2[i]:.3f}", ha='center', va='bottom')
# plt.savefig("x@y=6.png", bbox_inches='tight')

plt.show()
