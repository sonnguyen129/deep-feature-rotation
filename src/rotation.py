import tensorflow as tf
import numpy as np

def rotation_tensor(inputs, angles = None):
    """Rotate tensor in 90, 180, 270 angles"""
    final = copy.deepcopy(inputs)
    if angles == 90:
        for key, input in enumerate(inputs):
            input = input.numpy()
            input_shape = input.shape
            x90 = input.transpose((3, 2, 1 ,0)).reshape(input_shape)
            x90 = tf.convert_to_tensor(x90)
            final[key] = x90
        return final

    if angles == 180:
        for key, input in enumerate(inputs):
            input = input.numpy()
            input_shape = input.shape
            x180 = np.flip(input, 2)
            x180 = tf.convert_to_tensor(x180)
            final[key] = x180
        return final

    if angles == 270:
        for key, input in enumerate(inputs):
            input = input.numpy()
            input_shape = input.shape
            x90 = input.transpose((3, 2, 1 ,0)).reshape(input_shape)
            x270 = np.flip(x90, 3).reshape(input_shape)
            x270 = tf.convert_to_tensor(x270)
            final[key] = x90
        return final

    if angles not in [90, 180, 270]:
        raise ValueError('Invalid value')