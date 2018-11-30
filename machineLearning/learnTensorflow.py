import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt

encoded_size = 7

mnist = keras.datasets.mnist
(train,_),(test,_) = mnist.load_data()
train = train / 255.0
test = test / 255.0
train = train.reshape((len(train), np.prod(train.shape[1:])))
test = test.reshape((len(test), np.prod(test.shape[1:])))

input_img = keras.layers.Input(shape=(28*28,))
encoded = keras.layers.Dense(128,activation='relu')(input_img)
encoded = keras.layers.Dense(64,activation='relu')(encoded)
encoded = keras.layers.Dense(encoded_size,activation='relu')(encoded)
decoded = keras.layers.Dense(64,activation='relu')(encoded)
decoded = keras.layers.Dense(128,activation='relu')(decoded)
decoded = keras.layers.Dense(28*28,activation='sigmoid')(decoded)

autoencoder = keras.Model(input_img,decoded)

encoder = keras.Model(input_img,encoded)

encoded_input = keras.layers.Input(shape=(encoded_size,))
decoder_layer = autoencoder.layers[-3](encoded_input)
decoder_layer = autoencoder.layers[-2](decoder_layer)
decoder_layer = autoencoder.layers[-1](decoder_layer)
decoder = keras.Model(encoded_input,decoder_layer)

autoencoder.compile(optimizer='adam',loss='binary_crossentropy')

autoencoder.fit(train,train,
                epochs=40,
                batch_size=256,
                shuffle=True,
                validation_data=(test,test))

from matplotlib.widgets import Slider

start = 10.0
fig, ax = plt.subplots()
start_encoding = np.full((1,encoded_size),start)
im = plt.imshow(decoder.predict(start_encoding).reshape(28,28),cmap='Greys')
im.set_clim([0,1])
plt.axis('off')

def update(val):
    encoding = []
    for slider in sliders:
        encoding.append(slider.val)
    encoding = np.array(encoding).reshape(1,encoded_size)
    data = decoder.predict(encoding).reshape(28,28)
    im.set_data(data)
    fig.canvas.draw_idle()

sliders = []
for i in range(encoded_size):
    axcolor = plt.axes([0.05, 0.03 * i, 0.2, 0.025])
    slider = Slider(axcolor, str(i+1), 0.0, 30.0, valinit=start)
    slider.on_changed(update)
    sliders.append(slider)

plt.show()
