import tensorflow as tf
import numpy as np
import random

print("Starting program")

# inpuy matrix
data_input = np.zeros((0,23))

# output matrix
data_output = np.zeros((0,1))

#input file for the data
input_file = open("adult_norm.txt","r")

#read each line of the file and write the data into the matrices
for line in input_file:
    new_input = np.zeros((1,23))
   
    for i in range(23):
        new_input[0][i]= float(line.split(',')[i])
    data_output = np.append(data_output, [[float(line.split(',')[23])]], axis=0)
    data_input = np.append(data_input, new_input, axis=0)
                           
input_file.close()
print("Data aquired")

# inpuy matrix
test_input = np.zeros((0,23))

# output matrix
test_output = np.zeros((0,1))

# input file for the test cases
test_file = open("adult_test_norm.txt","r")

#read the file and write the data into the test matrices
for line in test_file:
    
    new_input = np.zeros((1,23))
   
    for i in range(23):
        new_input[0][i]= float(line.split(',')[i])
    test_output = np.append(test_output, [[float(line.split(',')[23])]], axis=0)
    test_input = np.append(test_input, new_input, axis=0)
                           
test_file.close()
print("Test dataset aquired")

# declare all variables for our model
# it has 3 layers
x = tf.placeholder(tf.float32, [None, 23])
W1 = tf.Variable(tf.random_uniform([23, 8]))
W2 = tf.Variable(tf.random_uniform([8, 1]))
b1 = tf.Variable(tf.zeros([8]))
b2 = tf.Variable(tf.zeros([1]))

# Execute the matrix multiplication and apply the activation funciton tanh
h1 = tf.tanh(tf.matmul(x, W1) + b1)
p = tf.tanh(tf.matmul(h1, W2) + b2)

# The expected output matrix
y = tf.placeholder(tf.float32, [None, 1])

# The learning rate of the Gradient Descent Optimizer
lr = 0.01

# The loss function for the model is the square difference between prediciton and known result
squared_deltas = tf.square(p - y)
loss = tf.reduce_mean(squared_deltas)
train_step = tf.train.GradientDescentOptimizer(lr).minimize(loss)

sess = tf.InteractiveSession()
tf.global_variables_initializer().run()

# Train
print("Starting training")

# Do 200000 iterations for training (best result if you increase this number)
for i in range(200000):
    
    # Create batches of 100 elements from the data matrices
    aslice = random.randint(0,len(data_input)-101)
    batch_xs = data_input[aslice:aslice+100]
    batch_ys = data_output[aslice:aslice+100]
    
    # Train the network with the batches
    sess.run(train_step, feed_dict={x: batch_xs, y: batch_ys})
    
    if i%20000 == 0:
        # Test trained model
        # The test is not executed in batches but with all the test cases altogether
        print("loss = ", sess.run(loss, feed_dict={x: test_input,
                                              y: test_output}))
        isPredictionCorrect = tf.less(tf.abs(p - y), 0.5)
        accuracy = tf.reduce_mean(tf.cast(isPredictionCorrect, tf.float32))
        print("accurancy = ", sess.run(accuracy, feed_dict={x: test_input,
                                                           y: test_output}))

