import os
from PIL import Image
from PIL import ImageFilter

base_img = Image.open("portrait.JPG")
img_filter = Image.open("filter3.jpg")
img_3= Image.open("filter.jpg")

size= (720,720) # always in tuples

base_img = base_img.resize(size)
img_filter = img_filter.resize(size)
img_3 = img_3.resize(size)

r,g,b = base_img.split()
R,G,B = img_filter.split()
Rr,Gg,Bb = img_3.split()

im = Image.merge("RGB",(r,b,Bb))
im.show()

#im.save('1_merged.jpg')