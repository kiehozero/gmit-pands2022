import numpy as np
import matplotlib.pyplot as plt

possibleCounties = np.array(["Maigh Eo","Gaillimh","Ros Comáin","Liatroma","Sligeach"])
# picks 100 randomly from possible counties with the frequency set in p
counties = np.random.choice(
    possibleCounties,
    p=[0.1,0.3,0.2,0.12,0.28],
    size=100
)

unique, counts = np.unique(counties, return_counts=True)

plt.pie(counts,labels=unique)

plt.show()