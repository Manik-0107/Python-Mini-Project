import numpy as np, matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 7))
ax.axis('off'); ax.set_aspect('equal')

plt.title("Happy Republic Day of India", fontsize=14, fontweight='bold')

t = np.linspace(0, 2*np.pi, 300)
ax.plot(.15*np.cos(t), .15*np.sin(t), '#0038A8')

for i in range(24):
    a = i*2*np.pi/24
    ax.plot([0, .15*np.cos(a)], [0, .15*np.sin(a)], '#0039A8')

x = np.linspace(-1.2, 1.2, 300)
ax.plot(x, .35*np.sin(x)+.55, lw=8, c='#FF9933')
ax.plot(x, .35*np.sin(x)-.55, lw=8, c='#138808')

y = np.linspace(-1, 1, 300)
ax.fill(.25*np.sin(2*y), y, '#0038A8')
plt.show()
