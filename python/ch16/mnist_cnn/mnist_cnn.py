import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.framework import graph_util
from tensorflow.python.platform import gfile

tf.logging.set_verbosity(tf.logging.ERROR)

mnist = input_data.read_data_sets("./MNIST_data/", one_hot=True)

#
# hyper parameters
#
learning_rate = 0.001
training_epochs = 20
batch_size = 100

#
# Model configuration
#
X = tf.placeholder(tf.float32, [None, 28, 28, 1], name='data')
Y = tf.placeholder(tf.float32, [None, 10])

conv1 = tf.layers.conv2d(X, 32, [3, 3], padding="same", activation=tf.nn.relu)
pool1 = tf.layers.max_pooling2d(conv1, [2, 2], strides=2, padding="same")

conv2 = tf.layers.conv2d(pool1, 64, [3, 3], padding="same", activation=tf.nn.relu)
pool2 = tf.layers.max_pooling2d(conv2, [2, 2], strides=2, padding="same")

flat3 = tf.contrib.layers.flatten(pool2)
dense3 = tf.layers.dense(flat3, 256, activation=tf.nn.relu)

logits = tf.layers.dense(dense3, 10, activation=None)
final_tensor = tf.nn.softmax(logits, name='prob')

cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(labels=Y, logits=logits))
optimizer = tf.train.AdamOptimizer(learning_rate).minimize(cost)

#
# Training
#
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    total_batch = int(mnist.train.num_examples / batch_size)

    print('Start learning!')
    for epoch in range(training_epochs):
        total_cost = 0

        for i in range(total_batch):
            batch_xs, batch_ys = mnist.train.next_batch(batch_size)
            batch_xs = batch_xs.reshape(-1, 28, 28, 1)
            _, cost_val = sess.run([optimizer, cost], feed_dict={
                                   X: batch_xs, Y: batch_ys})
            total_cost += cost_val

        print('Epoch:', '%04d' % (epoch + 1), 'Avg. cost = ',
              '{:.4f}'.format(total_cost/total_batch))

    print('Learning finished!')

    # Freeze variables and save pb file
    output_graph_def = graph_util.convert_variables_to_constants(
        sess, sess.graph_def, ['prob'])
    with gfile.FastGFile('./mnist_cnn.pb', 'wb') as f:
        f.write(output_graph_def.SerializeToString())

    print('Save done!')
