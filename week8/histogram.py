import numpy as np
import matplotlib.pyplot as plt

series = np.random.normal(size=10000)

plt.hist(series)

plt.show()