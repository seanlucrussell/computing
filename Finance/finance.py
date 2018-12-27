import time
import tensorflow as tf
import tensorflow.contrib.slim as slim
import numpy as np
import gym
env = gym.make('CartPole-v0')
gamma = 0.99
def discount_rewards(r):
    discounted_r = np.zeros_like(r)
    running_add = 0
    for t in reversed(range(0, r.size)):
        running_add = running_add * gamma + r[t]
        discounted_r[t] = running_add
    return discounted_r
class agent():
    def __init__(self, lr, s_size,a_size,h_size):
        self.state_in = tf.placeholder(shape=[None,s_size],dtype=tf.float32)
        hidden = slim.fully_connected(self.state_in,
                                      h_size,
                                      biases_initializer=None,
                                      activation_fn=tf.nn.relu)
        self.output = slim.fully_connected(hidden,
                                           a_size,
                                           activation_fn=tf.nn.softmax,
                                           biases_initializer=None)
        self.chosen_action = tf.argmax(self.output,1)
        self.reward_placeholder = tf.placeholder(shape=[None],dtype=tf.float32)
        self.action_placeholder = tf.placeholder(shape=[None],dtype=tf.int32)
        self.indexes = tf.range(0, tf.shape(self.output)[0])\
            * tf.shape(self.output)[1] + self.action_placeholder
        self.responsible_outputs = tf.gather(tf.reshape(self.output, [-1]), self.indexes)
        self.loss = -tf.reduce_mean(tf.log(self.responsible_outputs)*\
                                    self.reward_placeholder)
        tvars = tf.trainable_variables()
        self.gradient_placeholders = []
        for idx,var in enumerate(tvars):
            placeholder = tf.placeholder(tf.float32,name=str(idx)+'_placeholder')
            self.gradient_placeholders.append(placeholder)
        self.gradients = tf.gradients(self.loss,tvars)
        optimizer = tf.train.AdamOptimizer(learning_rate=lr)
        self.update_batch = optimizer.apply_gradients(zip(self.gradient_placeholders,
                                                          tvars))
        self.saver = tf.train.Saver()
tf.reset_default_graph()
myAgent = agent(lr=1e-2,s_size=4,a_size=2,h_size=8) 
total_episodes = 1000 
max_ep = 999
update_frequency = 5
env._max_episode_steps = max_ep
init = tf.global_variables_initializer()
with tf.Session() as sess:
    try:
        myAgent.saver.restore(sess,'./model.ckpt')
    except:
        sess.run(init)
    total_reward = []
    gradBuffer = sess.run(tf.trainable_variables())
    for ix,grad in enumerate(gradBuffer):
        gradBuffer[ix] = grad * 0
    for i in range(total_episodes):
        s = env.reset()
        running_reward = 0
        ep_history = []
        for j in range(max_ep):
            a_dist = sess.run(myAgent.output,feed_dict={myAgent.state_in:[s]})
            a = np.random.choice(a_dist[0],p=a_dist[0])
            a = np.argmax(a_dist == a)
            s1,r,d,_ = env.step(a) 
            ep_history.append([s,a,r])
            s = s1
            running_reward += r
            if d == True:
                ep_history = np.array(ep_history)
                ep_history[:,2] = discount_rewards(ep_history[:,2])
                feed_dict={myAgent.reward_placeholder:ep_history[:,2],
                           myAgent.action_placeholder:ep_history[:,1],
                           myAgent.state_in:np.vstack(ep_history[:,0])}
                grads = sess.run(myAgent.gradients, feed_dict=feed_dict)
                for idx,grad in enumerate(grads):
                    gradBuffer[idx] += grad
                if i % update_frequency == 0 and i != 0:
                    feed_dict = dict(zip(myAgent.gradient_placeholders, gradBuffer))
                    sess.run(myAgent.update_batch, feed_dict=feed_dict)
                    for ix,grad in enumerate(gradBuffer):
                        gradBuffer[ix] = grad * 0
                total_reward.append(running_reward)
                break
        if i % 100 == 0:
            print(np.mean(total_reward[-100:]))
    myAgent.saver.save(sess,'./model.ckpt')

with tf.Session() as sess:
    myAgent.saver.restore(sess,'./model.ckpt')
    s = env.reset()
    while True:
        a_dist = sess.run(myAgent.output,feed_dict={myAgent.state_in:[s]})
        a = np.random.choice(a_dist[0],p=a_dist[0])
        a = np.argmax(a_dist == a)
        #a = np.argmax(a_dist)
        env.render()
        s,_,d,_ = env.step(a)
        time.sleep(.01)
        if d:
            time.sleep(1.2)
            env.close()
            break
