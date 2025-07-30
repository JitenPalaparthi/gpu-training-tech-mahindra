import tensorflow as tf
import time

# Set matrix size (increase this to increase GPU load)
matrix_size = 4096

print("Checking GPU availability...")
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
print("Using GPU: ", tf.test.gpu_device_name())

# Generate two large random matrices
A = tf.random.normal([matrix_size, matrix_size])
B = tf.random.normal([matrix_size, matrix_size])

# Run matrix multiplication
print("Starting matrix multiplication workload...")
start = time.time()
C = tf.matmul(A, B)
#tf.experimental.numpy.linalg.norm(C)  # Some operation to use the result
print(C)
end = time.time()

print(f"Completed in {end - start:.2f} seconds.")