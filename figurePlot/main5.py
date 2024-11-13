import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(50000, 150000, 100001)
y = 50000/(49999*x*x+50000*x)
plt.plot(x, y)
plt.xlim(50000, 150000)
plt.xticks(np.linspace(50000, 150000, 6))
plt.xlabel("t")
plt.ylabel("h(t)")
plt.savefig("h(t).png", bbox_inches='tight')
plt.show()

# plt.figure(figsize=(8, 4))
# plt.stem(x2)
# plt.xticks(range(6), label_x2)
# plt.xlabel("X")
# plt.ylabel("PMF@Y=6")
# plt.ylim((0, 1))
# for i in range(len(x2)):
#     plt.text(i, x2[i], f"{x2[i]:.3f}", ha='center', va='bottom')
