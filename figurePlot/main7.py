import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(180, 500, 100000)
y = (((5*x)**0.5)/20-1.5)**20
for i, _ in enumerate(y):
    if y[i - 1] < 0.95 <= y[i]:
        f95 = x[i]
    if y[i - 1] < 0.99 <= y[i]:
        f99 = x[i]

plt.figure(figsize=(8, 4))
plt.plot(x, y)
plt.xlim(180, 500)
plt.ylim((0, 1))
plt.xticks(np.linspace(180, 500, 6))
plt.xlabel(r"$f$(kN)")
plt.ylabel(r"$F_{F_{max}}(f)$")
plt.grid(True)

plt.axvline(f95, color="red", linestyle="--", label=f"95th Percentile: {f95:.2f} kN")
plt.axvline(f99, color="purple", linestyle="--", label=f"99th Percentile: {f99:.2f} kN")
plt.legend()
plt.savefig("fmax.png", bbox_inches='tight')
plt.show()

# plt.figure(figsize=(8, 4))
# plt.stem(x2)
# plt.xticks(range(6), label_x2)
# plt.xlabel("X")
# plt.ylabel("PMF@Y=6")
# plt.ylim((0, 1))
# for i in range(len(x2)):
#     plt.text(i, x2[i], f"{x2[i]:.3f}", ha='center', va='bottom')
