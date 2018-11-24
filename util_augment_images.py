#!/usr/bin/python

#
# do run command "pip install Augmentor" first without quotes
#

import os, sys


import tensorflow as tf

#use absolute paths
ABS_PATh = os.path.dirname(os.path.abspath(__file__)) + "/"


flags = tf.app.flags
flags.DEFINE_string("dir_to_process", "", "dir_to_process")
FLAGS = flags.FLAGS

if FLAGS.dir_to_process == "":
    path = ""  #specify static here
else:
    path = "./data/"+FLAGS.dir_to_process+"/" 

import Augmentor
p = Augmentor.Pipeline(path)

p.rotate(probability=0.07, max_left_rotation=0.10, max_right_rotation=0.10)
p.zoom(probability=0.05, min_factor=0.11, max_factor=0.15)

p.sample(10000)