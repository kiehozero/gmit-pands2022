import numpy as np
import matplotlib.pyplot as plt

counties = np.array(["Maigh Eo","Gaillimh","Ros Comáin","Liatroma","Sligeach"])
titles = np.array([48,46,24,2,3])

plt.pie(titles)
plt.legend(counties)
plt.title("Connacht Football Champions")
plt.savefig("connacht.png")
plt.show()