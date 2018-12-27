import numpy as np

#data
inputs = np.array([[1],[2],[3],[4],[5]])
targets = inputs ** 3

def relu(x):
    return x * (x > 0)

def relu_derivative(x):
    return 1 * (x > 0)

#model
#w = np.random.random((inputs.shape[1]+1,targets.shape[1]))

hidden_layer_size = 8
w1 = np.random.random((inputs.shape[1]+1,hidden_layer_size))
w2 = np.random.random((hidden_layer_size+1,hidden_layer_size))
w3 = np.random.random((hidden_layer_size+1,targets.shape[1]))

#hyperparameters
iterations = 10000
learning_rate = .0001

#adding row of ones to front of data for bias
inputs_with_bias = np.insert(inputs,0,1,axis=1)

#training
for i in range(iterations):
    #prediction = relu(inputs_with_bias.dot(w))
    hidden_layer_1 = relu(inputs_with_bias.dot(w1))
    hidden_layer_1_with_bias = np.insert(hidden_layer_1,0,1,axis=1)
    hidden_layer_2 = relu(hidden_layer_1_with_bias.dot(w2))
    hidden_layer_2_with_bias = np.insert(hidden_layer_2,0,1,axis=1)

    prediction = relu(hidden_layer_2_with_bias.dot(w2))
    error = targets - prediction
    #delta_w = inputs_with_bias.T.dot(error * relu_derivative(prediction))
    #w += learning_rate * delta_w
    delta_w3 = hidden_layer_2_with_bias.T.dot(error * relu_derivative(prediction))
    delta_w2 = hidden_layer_1_with_bias.T.dot(error * relu_derivative(hidden_layer_2))
    delta_w1 = inputs_with_bias.T.dot(error * relu_derivative(hidden_layer_1))

    w3 += learning_rate * delta_w3
    w2 += learning_rate * delta_w2
    w1 += learning_rate * delta_w1
    if i % 100 == 0:
        print(prediction.transpose())
