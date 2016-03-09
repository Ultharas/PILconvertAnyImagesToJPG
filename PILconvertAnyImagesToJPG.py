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

def ConvertAllImagesTo(path, new_ext):
	tif_list = os.listdir(path)
	for tif_image in tif_list:

		old_ext = re.search('[^\.]+$', tif_image).group(0)
		if old_ext == new_ext:
			continue

		tif_path = os.path.join(path, tif_image)

		if imghdr.what(tif_path):

			im = image_post_open(tif_path)

			if im:

				if im.mode == "CMYK":
					im = im.convert("RGB")

				save_img_path = os.path.join(path, re.sub('[^\.]+$', new_ext, tif_image))
				try:
					im.save(save_img_path)
				except Exception as e:
					print type(e), e
				else:
					os.remove(tif_path)

ConvertAllImagesTo('export', 'jpg')

