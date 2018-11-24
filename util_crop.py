#!/usr/bin/python
from PIL import Image
import os, sys

import tensorflow as tf

#use absolute paths
ABS_PATh = os.path.dirname(os.path.abspath(__file__)) + "/"


flags = tf.app.flags
flags.DEFINE_string("dir_to_process", "", "dir_to_process")
flags.DEFINE_string("crop_top", "", "crop_top")
flags.DEFINE_string("crop_left", "", "crop_top")
flags.DEFINE_string("crop_width", "", "crop_top")
flags.DEFINE_string("crop_height", "", "crop_top")
FLAGS = flags.FLAGS

if FLAGS.dir_to_process == "":
    paths = []  #specify static here
else:
    paths = [ "./data/"+FLAGS.dir_to_process+"/" ]

def resize( path ):
    items = os.listdir( path )
    for item in items:
        print(item)
        if item == '.DS_Store':
            continue


        print('here 1')
        if os.path.isfile(path+item):
            print('here 2')
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imCrped = im.crop((int(FLAGS.crop_left), int(FLAGS.crop_top), int(FLAGS.crop_left)+int(FLAGS.crop_width), int(FLAGS.crop_top)+int(FLAGS.crop_height)))
            imCrped.save(f + '.' + e)

            print('here 3')
            #remove original 
            os.remove(path+item)

for path in paths:
    resize( path )
