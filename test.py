from PIL import Image
import os, sys

path = "./data/style/"
dirs = os.listdir( path )

def resize():
    for item in dirs:
        if os.path.isfile(path+item):
            im = Image.open(path+item)
            f, e = os.path.splitext(path+item)
            imResize = im.resize((512,422), Image.ANTIALIAS)
            imResize.save(f + '_resized.jpg', 'JPEG', quality=90)

resize()