#import Image from PIL
import os
from PIL import Image
from PIL import ImageFilter
#load Images into ogjects
base_img = Image.open("portrait.JPG")
img_filter = Image.open("filter3.jpg")
img_3= Image.open("filter.jpg")
#set O\P Image size
size= (760,760) # always in tuples
#resize all images to op size
base_img = base_img.resize(size)
img_filter = img_filter.resize(size)
img_3 = img_3.resize(size)
#split each image into RGB 
r,g,b = base_img.split()
R,G,B = img_filter.split()
Rr,Gg,Bb = img_3.split()
#merge RGB vectors from different images
im = Image.merge("RGB",(r,b,Bb))
im.show()

im.save("filtered.jpg","JPG")