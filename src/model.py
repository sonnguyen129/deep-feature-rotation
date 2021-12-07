import tensorflow as tf
import numpy as np
import PIL.Image
import time
import functools
import os
import copy
from rotation import rotation_tensor

def vgg_layers(layer_names):
    """ Creates a vgg model that returns a list of intermediate output values."""
    # Load our model. Load pretrained VGG, trained on imagenet data
    vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
    vgg.trainable = False
    
    outputs = [vgg.get_layer(name).output for name in layer_names]
    model   = tf.keras.Model([vgg.input], outputs)
    return model

def gram_matrix(input_tensor):
    result = tf.linalg.einsum('bijc,bijd->bcd', input_tensor, input_tensor)
    input_shape = tf.shape(input_tensor)
    num_locations = tf.cast(input_shape[1]*input_shape[2], tf.float32)
    return result/(num_locations)

class StyleContentModel(tf.keras.models.Model):
    def __init__(self, style_layers, content_layers):
        super(StyleContentModel, self).__init__()
        self.vgg =  vgg_layers(style_layers + content_layers)
        self.style_layers = style_layers
        self.content_layers = content_layers
        self.num_style_layers = len(style_layers)
        self.vgg.trainable = False

    def call(self, inputs):
        "Expects float input in [0,1]"
        inputs = inputs*255.0
        preprocessed_input = tf.keras.applications.vgg19.preprocess_input(inputs)
        outputs = self.vgg(preprocessed_input)
        style_outputs, content_outputs = (outputs[:self.num_style_layers], 
                                        outputs[self.num_style_layers:])

        style_outputs = [gram_matrix(style_output)
                        for style_output in style_outputs]

        content_dict = {content_name:value 
                        for content_name, value 
                        in zip(self.content_layers, content_outputs)}

        style_dict = {style_name:value
                    for style_name, value
                    in zip(self.style_layers, style_outputs)}
        
        return {'content':content_dict, 'style':style_dict}

class StyleContentModel_style(tf.keras.models.Model):
    def __init__(self, style_layers, content_layers, rotation_weight):
        super(StyleContentModel_style, self).__init__()
        self.vgg = vgg_layers(style_layers + content_layers)
        self.style_layers = style_layers
        self.content_layers = content_layers
        self.num_style_layers = len(style_layers)
        self.vgg.trainable = False
        self.rotation_weight = rotation_weight

    def call(self, inputs):
        "Expects float input in [0,1]"
        inputs = inputs*255.0
        preprocessed_input = tf.keras.applications.vgg19.preprocess_input(inputs)
        outputs = self.vgg(preprocessed_input)
        style_outputs, content_outputs = (outputs[:self.num_style_layers], 
                                        outputs[self.num_style_layers:])
        
        # Rotation
        style_outputs_90 = rotation_tensor(style_outputs, 90)
        style_outputs_180 = rotation_tensor(style_outputs, 180)
        style_outputs_270 = rotation_tensor(style_outputs, 270)
        
        style_outputs_1 = [gram_matrix(style_output)
                        for style_output in style_outputs]
        
        # Fusion
        style_outputs_2 = [(1 - self.rotation_weight) * gram_matrix(style_output1) + self.rotation_weight * gram_matrix(style_output2)
                        for style_output1, style_output2 in zip(style_outputs, style_outputs_90)]

        style_outputs_3 = [(1 - self.rotation_weight) * gram_matrix(style_output1) + self.rotation_weight * gram_matrix(style_output2)
                        for style_output1, style_output2 in zip(style_outputs, style_outputs_180)]

        style_outputs_4 = [(1 - self.rotation_weight) * gram_matrix(style_output1) + self.rotation_weight * gram_matrix(style_output2)
                        for style_output1, style_output2 in zip(style_outputs, style_outputs_270)]

        # Save feature
        content_dict = {content_name:value 
                        for content_name, value 
                        in zip(self.content_layers, content_outputs)}

        style_dict_1 = {style_name:value
                    for style_name, value
                    in zip(self.style_layers, style_outputs_1)}

        style_dict_2 = {style_name:value
                    for style_name, value
                    in zip(self.style_layers, style_outputs_2)}

        style_dict_3 = {style_name:value
                    for style_name, value
                    in zip(self.style_layers, style_outputs_3)}

        style_dict_4 = {style_name:value
                    for style_name, value
                    in zip(self.style_layers, style_outputs_4)}
        
        return {'content':content_dict, 'style_1':style_dict_1, 'style_2':style_dict_2, 'style_3':style_dict_3, 'style_4':style_dict_4}