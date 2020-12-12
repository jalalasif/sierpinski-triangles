# import matplotlib and choice
import matplotlib
import matplotlib.pyplot as plt
from random import choice


# Use this command to make sure the graph does not show up in another window iff jupyter notebook
# %matplotlib inline

# Sierpinski Triangle transformation methods
def tr1(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x
    y1 = 0.5 * y
    return x1, y1


def tr2(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 0.5
    y1 = 0.5 * y + 0.5
    return x1, y1


def tr3(p):
    x = p[0]
    y = p[1]
    x1 = 0.5 * x + 1
    y1 = 0.5 * y
    return x1, y1


# Use an iterative loop to randomly choose a transformation and print it out
transformations = [tr1, tr2, tr3]
a1 = [0]
b1 = [0]
a, b = 0, 0

num_triangles = int(input("Please input the number of triangles to generate: "))

for i in range(num_triangles):
    trans = choice(transformations)
    a, b = trans((a, b))
    a1.append(a)
    b1.append(b)

plt.rc('figure', figsize=(16, 16))
plt.plot(a1, b1, 'o')
plt.show()
