#!/usr/bin/python
from PIL import Image
import os, sys

#paths = [ "./data/datasetB4/Download/1/", "./data/datasetB4/Download/2/", "./data/datasetB4/Download/3/", "./data/datasetB4/Download/4/", "./data/datasetB4/Download/5/", "./data/datasetB4/Download/6/", "./data/datasetB4/Download/7/", "./data/datasetB4/Download/8/", "./data/datasetB4/Download/9/", "./data/datasetB4/Download/10/" ]
paths = [ "./data/arms/" ]

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
            imResize = im.resize((128,128), Image.ANTIALIAS)
            imResize.save(f + '.png', 'PNG', quality=90)

            print('here 3')
            #remove original 
#            os.remove(path+item)

for path in paths:
    dirs = os.listdir( path )
    resize( path )
