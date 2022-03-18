import numpy as np

salaryMin = 20000
salaryMax = 80000

# the seed() command stores the initial random selection so it is returned every time the program runs
np.random.seed(1)
salaries = np.random.randint(salaryMin,salaryMax,10)

# below will perform the operation on every item within the matrix
newSalaries = salaries + 5000

# identical results below, mine was the first, stated lab solution was second
perSalaries = ( salaries / 100 ) * 105
pcSalaries = salaries * 1.05

print(salaries)
print(newSalaries)
print(perSalaries)
print(pcSalaries)