import random
import matplotlib.pyplot as plt
num_points = int(input("Input amount of points:"))
x_inside = []
y_inside = []
x_outside = []
y_outside = []
inside_circle = 0
for i in range(num_points):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 <= 1:
       inside_circle += 1
       x_inside.append(x)
       y_inside.append(y)
    else:
       x_outside.append(x)
       y_outside.append(y)
plt.figure(figsize=(5, 5))
plt.scatter(x_inside, y_inside, color='blue', s=1)
plt.scatter(x_outside, y_outside, color='red', s=1)
print("Estimated value of pi:", 4 * inside_circle / num_points)
plt.show()


