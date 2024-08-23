import numpy as np
import matplotlib.pyplot as plt
from scipy import misc  # contains an image of a raccoon!
from PIL import Image  # for reading image files
import random

# chal1:
a = np.arange(10, 30)
print(a)
# [10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29]

# chal2:
print(a[-3:])
# [27 28 29]

b = a[[3,4,5]]
print(b)
# [13 14 15]

c = a[12:]
print(c)

# Filter the array to only include numbers divisible by 2
d = a[a % 2 == 0]
print(d)

# chal3:
# reverses the numbers in backwards order:
e = np.flip(a)
print(e)

# chal4:
f = [6, 0, 9, 0, 0, 5, 0]
filtered_f = [x for x in f if x != 0]
print(filtered_f)

# chal5:
# Generate a 3x3x3 array with random integers between 0 (inclusive) and 10 (exclusive)
random_int_array = np.random.randint(0, 10, size=(3, 3, 3))
print("Random 3x3x3 array with np.random.randint:")
print(random_int_array)

# chal6:
g = np.linspace(0, 100, num=9)
print(g)
print(g.shape)

# chal7:
import matplotlib.pyplot as plt

# Challenge 6: Create vector x of size 9 with values between 0 and 100
x = np.linspace(0, 100, 9)

# Challenge 7: Create vector y of size 9 with values between -3 and 3
y = np.linspace(-3, 3, 9)

# Plot x and y on a line chart
# plt.plot(x, y, marker='o')  # marker='o' adds a marker for each point on the line
# plt.title("Line chart of x vs. y")
# plt.xlabel("x values")
# plt.ylabel("y values")
# plt.grid(True)  # Adds a grid to the plot for better readability
# plt.show()


# chal 8:
# noise = np.random.rand(128, 128, 3)
# plt.imshow(noise)
# plt.title("Random Noise Image")
# plt.axis('off')  # Turn off axis labels
# plt.show()