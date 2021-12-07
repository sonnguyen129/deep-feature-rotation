import tensorflow as tf

import IPython.display as display

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False

import numpy as np
import PIL.Image
import time
import functools
import os
import copy
import argparse

def clip_0_1(image):
    return tf.clip_by_value(image, clip_value_min=0.0, clip_value_max=1.0)

@tf.function()
def train_step(image_1, image_2, image_3, image_4):
    with tf.GradientTape() as tape_1, tf.GradientTape() as tape_2, tf.GradientTape() as tape_3, tf.GradientTape() as tape_4:
        outputs_1 = extractor(image_1)
        outputs_2 = extractor(image_2)
        outputs_3 = extractor(image_3)
        outputs_4 = extractor(image_4)

        loss_1 = style_content_loss_1(outputs_1)
        loss_2 = style_content_loss_2(outputs_2)
        loss_3 = style_content_loss_3(outputs_3)
        loss_4 = style_content_loss_4(outputs_4)

        loss_1 += total_variation_weight*tf.image.total_variation(image_1)
        loss_2 += total_variation_weight*tf.image.total_variation(image_2)
        loss_3 += total_variation_weight*tf.image.total_variation(image_3)
        loss_4 += total_variation_weight*tf.image.total_variation(image_4)

    grad_1 = tape_1.gradient(loss_1, image_1)
    grad_2 = tape_2.gradient(loss_2, image_2)
    grad_3 = tape_3.gradient(loss_3, image_3)
    grad_4 = tape_4.gradient(loss_4, image_4)

    opt.apply_gradients([(grad_1, image_1)])
    opt.apply_gradients([(grad_2, image_2)])
    opt.apply_gradients([(grad_3, image_3)])
    opt.apply_gradients([(grad_4, image_4)])

    image_1.assign(clip_0_1(image_1))
    image_2.assign(clip_0_1(image_2))
    image_3.assign(clip_0_1(image_3))
    image_4.assign(clip_0_1(image_4))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inference model(Train + test process)')
    parser.add_argument('--content-image', type=str, default='data/content',
                        help='Content images directory for train')
    parser.add_argument('--style-image', type=str, default='data/style',
                        help='style images directory for train')
    parser.add_argument('--iter', type=int, default=3000,
                        help='Number of sweeps over the dataset to train')
    parser.add_argument('--snapshot_interval', type=int, default=100,
                        help='Interval of snapshot to generate image')
    parser.add_argument('--learning_rate', '-lr', type=int, default=0.02,
                        help='learning rate for Adam')
    parser.add_argument('--content-weight', type=int, default=1e4)
    parser.add_argument('--style-weight', type=int, default=1e-2)
    parser.add_argument('--total-variation-weight', type=int, default=30)
    parser.add_argument('--save_dir', type=str, default='result',
                        help='save directory for result and loss')

    args = parser.parse_args()

    vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
    content_layers = ['block5_conv2']
    style_layers   = ['block1_conv1',
                    'block2_conv1',
                    'block3_conv1', 
                    'block4_conv1', 
                    'block5_conv1']

    num_content_layers = len(content_layers)
    num_style_layers   = len(style_layers)

    image_1 = tf.Variable(content_image)
    image_2 = tf.Variable(content_image)
    image_3 = tf.Variable(content_image)
    image_4 = tf.Variable(content_image)

    import time
    start = time.time()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    epochs = 30
    steps_per_epoch = 100

    step = 0
    for n in range(epochs):
    for m in range(steps_per_epoch):
        step += 1
        train_step(image_1, image_2,image_3, image_4)
        print(".", end='')
    display.clear_output(wait=True)
    display.display(tensor_to_image(image_1))
    display.display(tensor_to_image(image_2))
    display.display(tensor_to_image(image_3))
    display.display(tensor_to_image(image_4))
    print("Train step: {}".format(step))

    fname_1 = f'{output_dir}/at_{n+1}_output1.png' 
    mpl.image.imsave(fname_1, image_1[0].numpy())

    fname_2 = f'{output_dir}/at_{n+1}_output2.png' 
    mpl.image.imsave(fname_2, image_2[0].numpy())

    fname_3 = f'{output_dir}/at_{n+1}_output3.png' 
    mpl.image.imsave(fname_3, image_3[0].numpy())

    fname_4 = f'{output_dir}/at_{n+1}_output4.png' 
    mpl.image.imsave(fname_4, image_4[0].numpy())

    end = time.time()
    print("Total time: {:.1f}".format(end-start))


