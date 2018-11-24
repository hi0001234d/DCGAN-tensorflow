#!/usr/bin/python
from PIL import Image
import os, sys

import tensorflow as tf

#use absolute paths
ABS_PATh = os.path.dirname(os.path.abspath(__file__)) + "/"


flags = tf.app.flags
flags.DEFINE_string("dir_to_process", "", "dir_to_process")
flags.DEFINE_string("resize_by", "", "crop_top")
flags.DEFINE_string("width", "", "crop_top")
flags.DEFINE_string("height", "", "crop_top")
FLAGS = flags.FLAGS

if FLAGS.dir_to_process == "":
    paths = []  #specify static here
else:
    paths = [ "./data/"+FLAGS.dir_to_process+"/" ]

def resize( path ):
    for item in dirs:
        print(item)
        if item == '.DS_Store':
            continue


        print('here 1')
        if os.path.isfile(path+item):
            print('here 2')
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize( ( int( int(FLAGS.width)/int(FLAGS.resize_by) ), int( int(FLAGS.height)/int(FLAGS.resize_by) ) ), Image.ANTIALIAS )
            imResize.save(f + '.png', 'PNG', quality=100)

            print('here 3')
            #remove original 
#            os.remove(path+item)

for path in paths:
    dirs = os.listdir( path )
    resize( path )
