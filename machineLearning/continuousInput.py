import numpy as np
import tensorflow as tf

learning_rate = 0.01

base_input = np.array([[1,-1,0]])

inputs = tf.placeholder(shape=[None,3], dtype=tf.float32)
initial_weights = np.random.random([3,3])
weights = tf.Variable(initial_weights, dtype=tf.float32)
result = tf.matmul(inputs,weights)
loss = tf.norm(result-inputs)
weights_grad = tf.gradients(loss,weights)[0]
weight_update = weights.assign(weights - weights_grad * learning_rate)

with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    for i in range(2000):
        next_input = np.random.randn() * base_input
        l,_ = sess.run([loss,weight_update], feed_dict = {inputs: base_input})
        print(l)
    print(sess.run(weights))
