import tensorflow as tf
import numpy as np
import PIL.Image
import time
import functools
import os
import copy

def calc_style_loss(outputs, style_targets, style_weight,
                    num_style_layers):
    style_outputs = outputs['style']
    style_loss = tf.add_n([tf.reduce_mean((style_outputs[name]-style_targets[name])**2) 
                           for name in style_outputs.keys()])
    style_loss *= style_weight / num_style_layers
    return style_loss

def calc_content_loss(outputs, content_targets, content_weight, 
                     num_content_layers):
    content_outputs = outputs['content']
    content_loss = tf.add_n([tf.reduce_mean((content_outputs[name]-content_targets[name])**2) 
                             for name in content_outputs.keys()])
    content_loss *= content_weight / num_content_layers
    return content_loss

def style_content_loss(outputs, style_targets, content_targets, 
                content_weight, style_weight, num_content_layers, num_style_layers):
    style_loss = calc_style_loss(outputs, style_targets, style_weight,
                    num_style_layers)
    content_loss = calc_content_loss(outputs, content_targets, content_weight, 
                     num_content_layers)
    return style_loss + content_loss

def total_variation_loss(image):
    x_deltas, y_deltas = high_pass_x_y(image)
    return tf.reduce_sum(tf.abs(x_deltas)) + tf.reduce_sum(tf.abs(y_deltas))

def high_pass_x_y(image):
    x_var = image[:, :, 1:, :] - image[:, :, :-1, :]
    y_var = image[:, 1:, :, :] - image[:, :-1, :, :]

    return x_var, y_var

