import os
import zipfile


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
            zip_ref = zipfile.ZipFile(path+item, 'r')
            zip_ref.extractall(path)
            zip_ref.close()

            print('here 3')
            #remove original 
            os.remove(path+item)


convert()

