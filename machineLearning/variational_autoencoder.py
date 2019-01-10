from tensorflow.keras.layers import Lambda, Input, Dense
from tensorflow.keras.models import Model
from tensorflow.keras.datasets import mnist
from tensorflow.keras.losses import binary_crossentropy
from tensorflow.keras import backend as K
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# MNIST dataset
(x_train, _), (x_test, _) = mnist.load_data()
original_dim = x_train.shape[1] * x_train.shape[2]
x_train = np.reshape(x_train, [-1, original_dim])
x_test = np.reshape(x_test, [-1, original_dim])
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# network parameters
latent_dim = 4
hidden_layer_size = 512
batch_size = 256
epochs = 1
beta = 1.0

# ENCODER
inputs = Input(shape=(original_dim,), name='encoder_input')
h1 = Dense(hidden_layer_size, activation='relu')(inputs)
z_mean = Dense(latent_dim, name='z_mean')(h1)
z_log_var = Dense(latent_dim, name='z_log_var')(h1)
def sampling(args):
    # use reparameterization trick to push the sampling out as input
    z_mean, z_log_var = args
    return z_mean + K.exp(0.5 * z_log_var) * K.random_normal(shape=K.shape(z_mean))
z = Lambda(sampling, name='z')([z_mean, z_log_var])
encoder = Model(inputs, [z_mean, z_log_var, z], name='encoder')
# DECODER
latent_inputs = Input(shape=(latent_dim,), name='z_sampling')
h2 = Dense(hidden_layer_size, activation='relu')(latent_inputs)
outputs = Dense(original_dim, activation='sigmoid')(h2)
decoder = Model(latent_inputs, outputs, name='decoder')
# FULL VARTIATIONAL AUTOENCODER
outputs = decoder(encoder(inputs)[2])
vae = Model(inputs, outputs, name='vae_mlp')
# VAE loss = reconstruction_loss + kl_loss
reconstruction_loss = binary_crossentropy(inputs,outputs) * original_dim
kl_loss = 0.5 * beta * (K.square(z_mean) + K.exp(z_log_var) - 1 - z_log_var)
kl_loss = K.sum(kl_loss, axis=-1)
vae_loss = K.mean(reconstruction_loss + kl_loss)
vae.add_loss(vae_loss)
vae.compile(optimizer='adam')
try:
    vae.load_weights('vae_mnist.h5')
except:
    vae.fit(x_train,
            epochs=epochs,
            batch_size=batch_size,
            validation_data=(x_test, None))
    vae.save_weights('vae_mnist.h5')

'''
create sliders and interactive charts. Automatically creates
and positions (not well) sliders based off of number of latent
variables specified in the hyperparameters.
'''
fig, ax = plt.subplots()
plt.axis('off')
# initial value of all the latent variables (and sliders)
start = 0.0
start_encoding = np.full((1,latent_dim),start)
# display reconstruced image
image = decoder.predict(start_encoding).reshape(28,28)
im = plt.imshow(image,cmap='Greys', vmin=0, vmax=1)

# update is called whenever the value of a slider changes
def update(val):
    encoding = []
    for slider in sliders:
        encoding.append(slider.val)
    encoding = np.array(encoding).reshape(1,latent_dim)
    data = decoder.predict(encoding).reshape(28,28)
    im.set_data(data)
    fig.canvas.draw_idle()

#this bit creates the sliders and positions them
sliders = []
for i in range(latent_dim):
    axcolor = plt.axes([0.05, 0.03 * i, 0.2, 0.025])
    slider = Slider(axcolor, str(i+1), -4.0, 4.0, valinit=start)
    slider.on_changed(update)
    sliders.append(slider)

plt.show()
