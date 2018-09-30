# import cairocffi
# import rsvg
from cairosvg import svg2png
import os
import subprocess


paths = [ "./data/datasetB4/Download/1/", "./data/datasetB4/Download/2/", "./data/datasetB4/Download/3/", "./data/datasetB4/Download/4/", "./data/datasetB4/Download/5/", "./data/datasetB4/Download/6/", "./data/datasetB4/Download/7/", "./data/datasetB4/Download/8/", "./data/datasetB4/Download/9/", "./data/datasetB4/Download/10/" ]

def convert( path ):
    for item in dirs:
        print(item)
        if item == '.DS_Store':
            continue


        print('here 1')
        if os.path.isfile(path+item):
            print('here 2')
            # img = cairo.ImageSurface(cairo.FORMAT_ARGB32, 640,480)

            # ctx = cairo.Context(img)

            # ## handle = rsvg.Handle(<svg filename>)
            # # or, for in memory SVG data:
            # with open(path+item, 'r') as myfile:
            #     data=myfile.read()

            #     handle= rsvg.Handle(None, data)

            #     handle.render_cairo(ctx)

            #     img.write_to_png(path+item+".jpg")

            # # import cairocffi as cairo
            # print(open(path+item, 'rb').read())
            # svg2png(open(path+item, 'rb').read(), write_to=open(path+item+'.png', 'wb'))

            try:
                inkscape_path = subprocess.check_output(["which", "inkscape"]).strip()
            except subprocess.CalledProcessError:
                print("ERROR: You need inkscape installed to use this script.")
                exit(1)

            export_width = "512"
            export_height = "512"

            args = [
                inkscape_path,
                "--without-gui",
                "-f", path+item,
                "--export-area-page",
                "-w", export_width,
                "-h", export_height,
                "--export-png=" + path+item+'.png'
            ]
            print(args)
            subprocess.check_call(args)

            print('here 3')
            #remove original 
            os.remove(path+item)

for path in paths:
    dirs = os.listdir( path )
    convert( path )

