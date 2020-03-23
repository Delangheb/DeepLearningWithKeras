# Verify that Tensorflow is working
import tensorflow as tf
import os
os.environ["TF_CPP_MIN_LOG_LEVEL"]="2"

# print version
print("Tensorflow version is " + str(tf.__version__))

# verify session works
hello = tf.constant('Hello from Tensorflow')

#tf.Session does not exist in TensoFlow 2.0
#sess = tf.Session()


tf.print(hello)
