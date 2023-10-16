import numpy as np
import matplotlib.pyplot as plt


def newton_method(f, df, x0, eps):
    x = x0
    f_values = []
    x_values = []

    while abs(f(x)) > eps:
        f_values.append(f(x))
        x_values.append(x)
        x = x - f(x) / df(x)

    return x, f_values, x_values


def f(x):
    return


def df(x):
    return


x0 = float(input("Введите начальное приближение: "))
eps = float(input("Введите требуемую точность вычисления: "))

x_sol, f_values, x_values = newton_method(f, df, x0, eps)

print("Корень уравнения: ", x_sol)

x_plot = np.linspace(min(x_values) - 1, max(x_values) + 1, 100)
f_plot = f(x_plot)

plt.plot(x_plot, f_plot, label='f(x)')
plt.scatter(x_values, f_values, color='red', label='Промежуточные точки')
plt.legend()
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()