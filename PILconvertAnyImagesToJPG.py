# -*- coding: utf-8 -*-
import os
import re
import sys
import imghdr
import PIL
from PIL import Image

def image_post_open(filename):
    with open(filename, "rb") as f:
        try:
            im = Image.open(f)
        except Exception as e:
            print type(e), e
            return False
        else:
            im.load()
            return im

def ConvertAllImagesTo(new_ext):
    image_list = os.listdir('import')
    for image in image_list:

        old_ext = re.search('[^\.]+$', image).group(0)
        if old_ext == new_ext:
            continue

        image_path = os.path.join('import', image)

        if imghdr.what(image_path):

            im = image_post_open(image_path)

            if im:

                if im.mode == "CMYK":
                    im = im.convert("RGB")

                save_img_path = os.path.join('export', re.sub('[^\.]+$', new_ext, image_path))
                print save_img_path
                sys.exit()
                try:
                    im.save(save_img_path)
                except Exception as e:
                    print type(e), e
                else:
                    os.remove(tif_path)

ConvertAllImagesTo('jpg')