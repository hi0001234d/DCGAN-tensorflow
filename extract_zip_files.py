import os
import zipfile


#paths = [ "./data/datasetB4/Download/1/", "./data/datasetB4/Download/2/", "./data/datasetB4/Download/3/", "./data/datasetB4/Download/4/", "./data/datasetB4/Download/5/", "./data/datasetB4/Download/6/", "./data/datasetB4/Download/7/", "./data/datasetB4/Download/8/", "./data/datasetB4/Download/9/", "./data/datasetB4/Download/10/" ]
paths = [ "./data/datasetB5/1/" ]

def convert( path ):
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


for path in paths:
    dirs = os.listdir( path )
    convert( path )
    
