check if tensorflow gpu is installedpython by CBT fan club        

import tensorflow as tf
print(tf.test.gpu_device_name())
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))

import tensorflow as tf
4
print("Num GPUs Available: ", len(tf.config.experimental.list_physical_devices('GPU')))
tensorflow check gpupython by Splendid Scarab on Dec 09 2020 Comment
3
1
tf.config.list_physical_devices('GPU')
tensorflow gpu testpython by Witty Whale on Jun 24 2020 Comment
1
1
tf.test.is_gpu_available(
2
  cuda_only=False, min_cuda_compute_capability=None
3
)
Source: www.tensorflow.org
python check my gpupython by Jittery Jay on Dec 05 2020 Comment
2
1
from tensorflow.python.client import device_lib
2
​
3
def get_available_gpus():
4
    local_device_protos = device_lib.list_local_devices()
5
    return [x.name for x in local_device_protos if x.device_type == 'GPU']
6
​
Source: stackoverflow.com
check gpu in tensorflowpython by Lazy Lizard         on Jul 22 2021 Comment
1
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

1
# For tensorflow 2:
2
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
3
​
4
# For tensorflow 1:
5
sess = tf.Session(config=tf.ConfigProto(log_device_placement=True))
Source: stackoverflow.com
