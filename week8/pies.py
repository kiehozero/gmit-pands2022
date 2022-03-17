import numpy as np
import matplotlib.pyplot as plt

fruit = np.array(["apple","banana","lemon","orange"])

numbers = np.array([141,223,165,192])

plt.pie(numbers, labels=numbers)

plt.legend(fruit)

plt.savefig("pies.png")