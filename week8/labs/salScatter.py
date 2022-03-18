import matplotlib.pyplot as plt
import numpy as np

ageMin = 21
ageMax = 65
entries = 10
salaryMin = 20000
salaryMax = 80000

# the seed() command stores the initial random selection so it is returned every time the program runs
np.random.seed(1)
salaries = np.random.randint(salaryMin,salaryMax,entries)
ages = np.random.randint(ageMin,ageMax,entries)

print(ages, salaries)
plt.scatter(ages, salaries, label="salaries")
plt.legend()
plt.title("Salaries of OurEmployees")
plt.savefig("prettier-plot.png")