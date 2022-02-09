import tensorflow as tf
import numpy as np
import PIL.Image
import time
import functools
import os
import copy
import argparse
from dfr.model import StyleContentModel, StyleContentModel_style
from dfr.loss import style_content_loss
from dfr.utils import load_img, tensor_to_image
from dfr.function import train_step

import matplotlib.pyplot as plt
import matplotlib as mpl
mpl.rcParams['figure.figsize'] = (12,12)
mpl.rcParams['axes.grid'] = False

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Inference model(Train + test process)')
    parser.add_argument('--content-path', type=str, default='data/content/golden_gate.jpg',
                        help='Content images directory for train')
    parser.add_argument('--style-path', type=str, default='data/style/styles-97.jpg',
                        help='style images directory for train')
    parser.add_argument('--iter', type=int, default=3000,
                        help='Number of sweeps over the dataset to train')
    parser.add_argument('--snapshot_interval', type=int, default=100,
                        help='Interval of snapshot to generate image')
    parser.add_argument('--learning_rate', '-lr', type=int, default=0.02,
                        help='learning rate for Adam')
    parser.add_argument('--rotation-weight', type=int, default=1.0,
                        help='Rotation weight apply for intermediate features')                   
    parser.add_argument('--content-weight', type=int, default=1e4)
    parser.add_argument('--style-weight', type=int, default=1e-2)
    parser.add_argument('--total-variation-weight', type=int, default=30)
    parser.add_argument('--save-dir', type=str, default='results',
                        help='save directory for result and loss')

    args = parser.parse_args()

    content_image = load_img(args.content_path)
    style_image = load_img(args.style_path)

    output_name = args.content_path.split('/')[-1].replace('.jpg','') + "_" + \
                args.style_path.split('/')[-1].replace('.jpg','') + f'_{args.rotation_weight}'
    output_dir = f'{args.save_dir}/{output_name}'

    vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
    content_layers = ['block5_conv2']
    style_layers   = ['block1_conv1',
                    'block2_conv1',
                    'block3_conv1', 
                    'block4_conv1', 
                    'block5_conv1']

    num_content_layers = len(content_layers)
    num_style_layers   = len(style_layers)

    extractor_style = StyleContentModel_style(style_layers, content_layers, 
                            rotation_weight = args.rotation_weight)
    extractor       = StyleContentModel(style_layers, content_layers)

    style_targets_1 = extractor_style(style_image)['style_1']
    style_targets_2 = extractor_style(style_image)['style_2']
    style_targets_3 = extractor_style(style_image)['style_3']
    style_targets_4 = extractor_style(style_image)['style_4']
    style_targets_lst = [style_targets_1, style_targets_2, style_targets_3, style_targets_4]
    content_targets = extractor(content_image)['content']

    opt = tf.optimizers.Adam(learning_rate=args.learning_rate, beta_1=0.99, epsilon=1e-1)

    image_1 = tf.Variable(content_image)
    image_2 = tf.Variable(content_image)
    image_3 = tf.Variable(content_image)
    image_4 = tf.Variable(content_image)
    image_lst = [image_1, image_2, image_3, image_4]

    import time
    start = time.time()

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    step = 0
    for n in range(args.iter):
        step += 1
        print("Train step: {}".format(step))
        train_step(image_lst, style_targets_lst, extractor, opt, args.total_variation_weight, content_targets,
                args.content_weight, args.style_weight, num_content_layers, num_style_layers)

        if step % args.snapshot_interval == 0:
            fname_1 = f'{output_dir}/at_{step}_output1.png' 
            mpl.image.imsave(fname_1, image_1[0].numpy())

            fname_2 = f'{output_dir}/at_{step}_output2.png' 
            mpl.image.imsave(fname_2, image_2[0].numpy())

            fname_3 = f'{output_dir}/at_{step}_output3.png' 
            mpl.image.imsave(fname_3, image_3[0].numpy())

            fname_4 = f'{output_dir}/at_{step}_output4.png' 
            mpl.image.imsave(fname_4, image_4[0].numpy())

    end = time.time()
    print("Total time: {:.1f}".format(end-start))


