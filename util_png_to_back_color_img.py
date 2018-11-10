import os
import numpy as np
import cv2

import tensorflow as tf

flags = tf.app.flags
flags.DEFINE_string("source_img", '', "source_img ['']")
flags.DEFINE_integer("background_color", 255, "background_color [255]")
FLAGS = flags.FLAGS

res = {}
res["type"] = "success"
res["msg"] = ""

def remove_transparency(source, background_color):
    source_img = cv2.cvtColor(source[:,:,:3], cv2.COLOR_BGR2GRAY)
    source_mask = source[:,:,3]  * (1 / 255.0)

    background_mask = 1.0 - source_mask

    bg_part = (background_color * (1 / 255.0)) * (background_mask)
    source_part = (source_img * (1 / 255.0)) * (source_mask)

    return np.uint8(cv2.addWeighted(bg_part, 255.0, source_part, 255.0, 0.0))

# img = cv2.imread(FLAGS.source_img, -1)
# result = remove_transparency(img, FLAGS.background_color)


from PIL import Image

# image = Image.open(FLAGS.source_img)
# image.convert("RGBA") # Convert this to RGBA if possible

# canvas = Image.new('RGBA', image.size, (255,255,255,255)) # Empty canvas colour (r,g,b,a)
# canvas.paste(image, mask=image) # Paste the image onto the canvas, using it's alpha channel as mask
# canvas.thumbnail([width, height], PyImage.ANTIALIAS)
# canvas.save(FLAGS.source_img, format="PNG")


# card = Image.new("RGBA", (220, 220), (255, 255, 255))
# img = Image.open(FLAGS.source_img).convert("RGBA")
# x, y = img.size
# card.paste(img, (0, 0, x, y), img)
# card.save(FLAGS.source_img, format="png")


# image = Image.open(FLAGS.source_img)
# image.convert("RGBA") # Convert this to RGBA if possible

# pixel_data = image.load()

# if True or image.mode == "RGBA":
#   # If the image has an alpha channel, convert it to white
#   # Otherwise we'll get weird pixels
#   for y in range(image.size[1]): # For each row ...
#     for x in range(image.size[0]): # Iterate through each column ...
#       # Check if it's opaque
#       if True or pixel_data[x, y][3] < 255:
#         # Replace the pixel data with the colour white
#         print("got here 1")
#         pixel_data[x, y] = (255, 255, 255, 255)

# # Resize the image thumbnail
# # image.thumbnail([resolution.width, resolution.height], Image.ANTIALIAS)
# image.save(FLAGS.source_img + "2.png") 


image = cv2.imread(FLAGS.source_img)
r = 150.0 / image.shape[1]
dim = (150, int(image.shape[0] * r))
resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
lower_white = np.array([80, 1, 1],np.uint8) #lower hsv value
upper_white = np.array([130, 255, 255],np.uint8) #upper hsv value
hsv_img = cv2.cvtColor(resized,cv2.COLOR_BGR2HSV) #rgb to hsv color space
#filter the background pixels
frame_threshed = cv2.inRange(hsv_img, lower_white, upper_white) 

kernel = np.ones((5,5),np.uint8) 
#dilate the resultant image to remove noises in the background
#Number of iterations and kernal size will depend on the backgound noises size
dilation = cv2.dilate(frame_threshed,kernel,iterations = 2)
resized[dilation==255] = (0,0,0) #convert background pixels to black color
cv2.imshow('res', resized)
cv2.waitKey(0)

print(res)