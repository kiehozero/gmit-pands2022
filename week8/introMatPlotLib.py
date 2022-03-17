import numpy as np
import matplotlib.pyplot as plt

xpoints = np.array(range(1,101))
ypoints = xpoints * xpoints

# can plot multiple items in one file
plt.plot(xpoints,ypoints,label="test label")
plt.plot(xpoints,xpoints,label="straight", color="blue")
plt.legend()

# saves file to current location, using show() will open the file
plt.savefig("fig1.png")
