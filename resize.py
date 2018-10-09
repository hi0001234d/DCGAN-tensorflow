#!/usr/bin/python
from PIL import Image
import os, sys

path = "./data/datasetB2/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        print(item)
        if item == '.DS_Store':
            continue


        print('here 1')
        if os.path.isfile(path+item):
            print('here 2')
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((128,128), Image.ANTIALIAS)
            imResize.save(f + ' resized.jpg', 'JPEG', quality=90)

            print('here 3')
            #remove original 
            os.remove(path+item)

resize()