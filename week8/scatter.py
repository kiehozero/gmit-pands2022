import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
randomPoints = np.random.randint(1,1000, 100)

plt.scatter(xpoints,randomPoints,label="random")

plt.legend()
plt.savefig("scatter.png")