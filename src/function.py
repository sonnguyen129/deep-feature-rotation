import tensorflow as tf
import numpy as np
import PIL.Image
import time
import functools
import os
import copy
import argparse
from loss import style_content_loss

def clip_0_1(image):
return tf.clip_by_value(image, clip_value_min=0.0, clip_value_max=1.0)

@tf.function()
def train_step(image, style_targets, extractor, opt, total_variation_weight, content_targets, 
                content_weight, style_weight, num_content_layers, num_style_layers):
    """
    Params:
    image(list): List of output images(initialized)
    style_targets(list): List of style targets
    extractor: model is used to extract high-level representations derived from the content and style image.
    opt: optimizer(Adam)

    Returns:
    Generated images after optimizing process
    """
    with tf.GradientTape() as tape_1, tf.GradientTape() as tape_2, \
        tf.GradientTape() as tape_3, tf.GradientTape() as tape_4:

        outputs_1 = extractor(image[0])
        outputs_2 = extractor(image[1])
        outputs_3 = extractor(image[2])
        outputs_4 = extractor(image[3])

        loss_1 = style_content_loss(outputs_1, style_targets[0], content_targets, 
                        content_weight, style_weight,num_content_layers, num_style_layers)
        loss_2 = style_content_loss(outputs_2, style_targets[1], content_targets, 
                        ontent_weight, style_weight,num_content_layers, num_style_layers)
        loss_3 = style_content_loss(outputs_3, style_targets[2], content_targets, 
                        content_weight, style_weight,num_content_layers, num_style_layers)
        loss_4 = style_content_loss(outputs_4, style_targets[3], content_targets, 
                        content_weight, style_weight,num_content_layers, num_style_layers)

        loss_1 += total_variation_weight*tf.image.total_variation(image[0])
        loss_2 += total_variation_weight*tf.image.total_variation(image[1])
        loss_3 += total_variation_weight*tf.image.total_variation(image[2])
        loss_4 += total_variation_weight*tf.image.total_variation(image[3])

    grad_1 = tape_1.gradient(loss_1, image[0])
    grad_2 = tape_2.gradient(loss_2, image[1])
    grad_3 = tape_3.gradient(loss_3, image[2])
    grad_4 = tape_4.gradient(loss_4, image[3])

    opt.apply_gradients([(grad_1, image[0])])
    opt.apply_gradients([(grad_2, image[1])])
    opt.apply_gradients([(grad_3, image[2])])
    opt.apply_gradients([(grad_4, image[3])])

    image[0].assign(clip_0_1(image[0]))
    image[1].assign(clip_0_1(image[1]))
    image[2].assign(clip_0_1(image[2]))
    image[3].assign(clip_0_1(image[3]))