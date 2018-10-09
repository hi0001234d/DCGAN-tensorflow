from PIL import Image
import os


path = "./data/datasetB2/"
dirs = os.listdir( path )

def convert():
    for item in dirs:
        print(item)
        if item == '.DS_Store':
            continue


        print('here 1')
        if os.path.isfile(path+item):
            print('here 2')

            im = Image.open(path+item)
            rgb_im = im.convert('RGB')
            rgb_im.save(path+item+'.jpg')


            print('here 3')
            #remove original 
            os.remove(path+item)


convert()

