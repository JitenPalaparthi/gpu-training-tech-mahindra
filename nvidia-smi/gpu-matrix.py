import tensorflow as tf

import time

print(tf.config.list_physical_devices())

matrix_size = 8192

A = tf.random.normal((matrix_size, matrix_size))
B = tf.random.normal((matrix_size, matrix_size))

start_time = time.time()

with tf.device('/GPU:0'):
  C = tf.matmul(A,B)


print("Matrix Multiplication on CPU:",time.time()-start_time,"Seconds")

