#!/usr/bin/env python3
import pyqrcode
#import png
from PIL import Image
s = "https://python.plainenglish.io/" # url to open after scanning qr code
url = pyqrcode.create(s) # creating qr code
img = "python-in-plain-english.png" # name of image
url.png(img, scale=10) # saving image as png
im=Image.open(img) # opening image
im.show()