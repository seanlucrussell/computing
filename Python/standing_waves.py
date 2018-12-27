import math
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.widgets import Slider
from matplotlib import animation

width = 19 * np.pi
fig,ax = plt.subplots()

reflection = 50.0

def create_wave(i,reflection):
    w = np.sin(np.linspace(reflection + i * width, reflection + (i + 1) * width))
    if i % 2 == 1:
        w = np.flip(w,axis=0)
    return w

def create_waves(reflection):
    waves = [create_wave(0,reflection),
             create_wave(1,reflection)]
    i = 2
    while not math.isclose(waves[0][0],waves[-1][0],abs_tol=0.05):
        waves += [create_wave(i,reflection),create_wave(i+1,reflection)]
        i += 2
    return np.array(waves)

waves = create_waves(reflection)
total_wave = np.sum(waves,axis=0)

max_height = 2 * max(np.max(np.abs(total_wave)),np.max(np.abs(waves)))
ax = plt.axes(xlim=(0, 50), ylim=(-max_height, max_height))

plots = []
for wave in waves:
    plot, = ax.plot(wave,animated=True)
    plots.append(plot)
total_wave_plot, = ax.plot(total_wave,animated=True)

def init():
    return plots + [total_wave_plot]

def animate(i):
    reflection = i * 0.1
    waves = create_waves(reflection)
    for plot,wave in zip(plots,waves):
        plot.set_ydata(wave)
    total_wave = np.sum(waves,axis=0)
    total_wave_plot.set_ydata(total_wave)
    return plots + [total_wave_plot]
anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=31400, interval=20, blit=True)
plt.show()
