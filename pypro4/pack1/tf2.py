# tf에서 변수 선언 후 사용
import tensorflow as tf

f = tf.Variable(1.0)
v = tf.Variable(tf.ones((2,)))
m = tf.Variable(tf.ones((2,1)))
print(f)
print(v)
print(m)


