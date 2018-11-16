import tensorflow as tf
import numpy as np
from tensorflow import keras
import datetime as dt
import pandas as pd
import pandas_datareader.data as web
import matplotlib.pyplot as plt

start = dt.datetime(2013,1,1)
end = dt.datetime.now()
raw_data = web.DataReader("AAPL", 'iex', start, end).values

data = raw_data[:-1,1].reshape(-1,1,1)
targets = raw_data[1:,1].reshape(-1,1)

model = keras.Sequential()
model.add(keras.layers.BatchNormalization())
model.add(keras.layers.SimpleRNN(units=200))
model.add(keras.layers.Dense(units=100))
model.add(keras.layers.Dense(units=50))
model.add(keras.layers.Dense(targets.shape[1]))
model.compile(loss='mean_squared_error', optimizer='adam')
model.fit(data, targets, epochs=50, verbose=2)

scores = model.evaluate(data, targets)
print("\n%s: %.2f%%" % (model.metrics_names[0], scores*100))

def make_predictions(sequence, number_of_samples):
    prediction_input = sequence[:number_of_samples]
    plt.plot(sequence.reshape(-1))
    plt.axvline(x=number_of_samples)
    prediction = prediction_input
    prediction = np.append(prediction[:-1],model.predict(prediction[:-1])[-1].reshape(-1,1,1)).reshape(-1,1,1)
    for i in range(len(sequence) - number_of_samples):
        prediction = np.append(prediction,model.predict(prediction[-1].reshape(-1,1,1)).reshape(-1,1,1)).reshape(-1,1,1)
    plt.plot(prediction.reshape(-1))
    plt.show()

make_predictions(data,1000)
