import numpy as np
import matplotlib.pyplot as plt

# dataset
# height = [3, 12, 5, 18, 23, 5, 7, 25, 14]
bars = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')
y_pos = np.arange(len(bars))


def run(height):
    # Create bars and choose color
    plt.bar(y_pos, height, color=(0.5, 0.1, 0.5, 0.6))

    # Add title and axis names
    plt.title('Bar Chart')
    plt.xlabel('categories')
    plt.ylabel('values')

    # Limits for the Y axis
    plt.ylim(0, 30)

    # Create names
    plt.xticks(y_pos, bars)

    # Show graphic
    plt.show()

