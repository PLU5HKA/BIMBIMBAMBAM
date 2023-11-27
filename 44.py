import csv
import numpy as np
import openpyxl
import matplotlib.pyplot as plt
from scipy.interpolate import make_interp_spline
from scipy.interpolate import interp1d
def func(x, a, b, c):
    return a * np.exp(-b * x) + c

def convert_to_float(s):
    s = s.replace(',', '.')
    f = float(s)
    return f

def trapezoidal_rule(x, y):
    n = len(x)
    integral = 0.0
    for i in range(1, n):
        integral += (x[i] + x[i - 1]) * (y[i] - y[i - 1]) / 2.0
    return integral

def read_xlsx_file(file_name):
    wb = openpyxl.load_workbook(file_name)
    sheet = wb.active
    H = []
    B = []

    for row in sheet.iter_rows(values_only=True):
        H.append(round(row[0]))
        B.append(round(row[1]))

    return H, B


C1 = (1560 * 4 * 3.14) / (5.6 * 0.3  * 1000)
C2 = (6800 * 0.000022*10000)/(300*0.000314)
with open('LBB.csv') as f:
    reader = csv.reader(f, delimiter=';')
    x = []
    y = []
    for row in reader:
        x.append(convert_to_float(row[1]) * C1)
        y.append((convert_to_float(row[2]) / 1000)*C2)

plt.figure(1)
plt.plot(x, y)
plt.title("S")
plt.xlabel("H")
plt.ylabel("B")
plt.grid(True)


H, B = read_xlsx_file("mmc.xlsx")

plt.figure(3)
plt.title('MMC PLOT')
plt.plot(H, B)
plt.xlabel('H')
plt.ylabel('B')

# cubic_interpolation_model = interp1d(H, B, kind="cubic")
#
# H_ = np.linspace(min(H), max(H), 500)
# B_ = cubic_interpolation_model(H_)
#
# plt.figure(2)
# plt.plot(H_, B_)
# plt.title("Plot Smooth Curve Using the scipy.interpolate.interp1d Class")
# plt.xlabel("H")
# plt.ylabel("B")

dB = []
for i in range(len(B)-1):
    dB.append(round((B[i+1]-B[i]) / (H[i+1] - H[i]), 2))
H.pop()
plt.figure(4)
plt.title('DIFF MMC')
plt.plot(H, dB)
plt.xlabel('H')
plt.ylabel('dB')

l = 30
r = 0.1
V = 3.14 * r * r * l
integral = trapezoidal_rule(x, y)
print("S=", round(integral, 5)/(4 * 3.14))
print("Потери энергии, Дж:", round(integral * 1E-7 * 50 * V, 10))
print("μ=", max(dB))
plt.show()

