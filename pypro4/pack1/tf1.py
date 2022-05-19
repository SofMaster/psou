# DeepLearning library : TensorFlow

# 텐서플로우의 이해
import tensorflow as tf
print(tf.__version__)

# 상수 정의
print(1, type(1))
print([1], type([1]))
print(tf.constant(1), type(tf.constant(1)))  # scalar 0 D tensor
print(tf.constant([1]))   # vector, 1 D tensor 
print(tf.constant([[1]]))  # matrix, 2 D tensor
print(tf.rank(tf.constant([[1]])))

print()
a = tf.constant([1, 2])
b = tf.constant([3, 4])
c = a + b
d = tf.add(a, b)
print(c, type(c))
print(d, type(d))
# e = tf.constant([3])
# e = tf.constant(3)
e = tf.constant([[3]])  # 큰 차원으로 형변환
f = c + e  # broadcast 연산 
print(f)

print()
print(7, type(7))
print(tf.convert_to_tensor(7, dtype=tf.float32))
print(tf.cast(7, dtype=tf.float32))
print(tf.constant(7, dtype=tf.float32))
print(tf.constant(7.0))
print()

import numpy as np
arr = np.array([1, 2, 3])
print(arr, type(arr))
tfarr = tf.add(arr, 5)
print(tfarr)
print(tfarr.numpy())      # numpy type으로 형변환(강제)
print(np.add(tfarr, 3))  # numpy type으로 형변환(자동)  [ 9 10 11] ndarray type

print(list(tfarr.numpy()))  # [6, 7, 8]  list type




