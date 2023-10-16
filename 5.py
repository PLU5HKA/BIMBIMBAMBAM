import sympy as sp
from scipy import integrate
# Аналитически
x = sp.Symbol('x')
f = str(input('f(x)='))
a = str(input("a="))
b = str(input("b="))
print(sp.integrate(f,(x,a,b)))
# Численно
f2 = str(input('f2(x)='))
a2 = float(input("a2="))
b2 = float(input("b2="))
integral, error = integrate.quad(lambda x:eval(f2), a2, b2)
print(integral)