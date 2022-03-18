import matplotlib.pyplot as plt
import numpy as np

salaryMin = 20000
salaryMax = 80000

# the seed() command stores the initial random selection so it is returned every time the program runs
np.random.seed(1)
salaries = np.random.randint(salaryMin,salaryMax,10)

print(salaries)
plt.hist(salaries)

plt.show()