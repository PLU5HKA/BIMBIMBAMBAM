import numpy as np
import scipy.fftpack
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

dt = 0.001
t = np.arange(0.0, 2*np.pi, dt)

s1 = 5*np.sin(1.03*t)
s2 = -3*np.sin(3*t)
s3 = -2*np.sin(5*t)
signal = (s1 + s2 + s3)/3
noise = (np.random.random(t.shape) - 0.5)*np.random.random(t.shape)*10
ys = signal + noise

plt.plot(t, ys, 'gray')
plt.plot(t, signal, 'yellow')
plt.title('Signal')
plt.xlabel('t')
plt.ylabel('Amplitude')
yellow_patch = mpatches.Patch(color='yellow', label='Generated')
gray_patch = mpatches.Patch(color='gray', label='Transmitted')
plt.legend(handles=[yellow_patch, gray_patch])
plt.show()
sf = scipy.fftpack.rfft(ys)

freqs = t/(2*dt)
plt.subplot(111)
plt.plot(freqs, np.absolute(sf)*dt, 'red')
plt.title('Fourier spectrum')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

border = np.amax(np.absolute(sf))*0.10
sf_cut = sf.copy()
sf_cut[np.absolute(sf)<border] = 0

plt.subplot(111)
plt.plot(freqs, np.absolute(sf_cut)*dt, 'red')
plt.title('Fourier spectrum after cut')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

isf = scipy.fftpack.irfft(sf_cut)
plt.plot(t, ys, 'gray')
plt.plot(t, isf, 'black')
plt.plot(t, signal, 'yellow')
plt.title('Signal')
plt.xlabel('t')
plt.ylabel('Amplitude')
yellow_patch = mpatches.Patch(color='yellow', label='Generated')
gray_patch = mpatches.Patch(color='gray', label='Transmitted')
black_patch = mpatches.Patch(color='black', label='Noise filtered')
plt.legend(handles=[yellow_patch, gray_patch, black_patch])
plt.show()