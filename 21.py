import numpy as np
import matplotlib.pyplot as plt
import math

function = input("Введите функцию: ")

# Создание массива значений x
x = np.linspace(0, 2*np.pi, 100)

# Вычисление значений функции
y = eval(function, {'x': x, 'sin': np.sin, 'cos': np.cos, 'tan': np.tan})

# Построение графика в декартовых координатах
plt.figure(1)
plt.plot(x, y)
plt.title('График функции в декартовых координатах')
plt.xlabel('x')
plt.ylabel('y')

# Построение графика в полярных координатах
r = y
theta = x
plt.figure(2)
ax = plt.subplot(111, projection='polar')
ax.plot(theta, r)
ax.set_title('График функции в полярных координатах')

plt.show()