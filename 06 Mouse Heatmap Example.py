import matplotlib.pyplot as plt
import random

x = [random.randint(0, 100) for _ in range(200)]
y = [random.randint(0, 100) for _ in range(200)]

plt.hexbin(x, y, gridsize=20, cmap="inferno")
plt.colorbar(label="Density")
plt.title("Mouse Heatmap Exampele")
plt.show()
