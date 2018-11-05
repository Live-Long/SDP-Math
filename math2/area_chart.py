import numpy as np
import matplotlib.pyplot as plt

# create data
x = range(1, 15)
y = [1, 4, 6, 8, 4, 5, 3, 2, 4, 1, 5, 6, 8, 7]

# Change the color and its transparency
plt.fill_between(x, y, color="skyblue", alpha=0.4)
plt.show()

# Same, but add a stronger line on top (edge)
plt.fill_between(x, y, color="skyblue", alpha=0.2)
plt.plot(x, y, color="Slateblue", alpha=0.6)

import seaborn as sns

# Make the same graph
plt.fill_between(x, y, color="skyblue", alpha=0.3)
plt.plot(x, y, color="skyblue")

# Add titles
plt.title("An area chart", loc="left")
plt.xlabel("Value of X")
plt.ylabel("Value of Y")


plt.show()