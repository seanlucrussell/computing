import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.25)
start_color = 1.0
im = plt.imshow(np.full((28,28),start_color),cmap='Greys')
im.set_clim([0,255])

axcolor = plt.axes([0.25, 0.1, 0.65, 0.03])
color_slider = Slider(axcolor, 'Color', 0.0, 255.0, valinit=start_color)

def update(val):
    color = color_slider.val
    data = np.full((28,28),color)
    im.set_data(data)
    fig.canvas.draw_idle()
color_slider.on_changed(update)

plt.show()
