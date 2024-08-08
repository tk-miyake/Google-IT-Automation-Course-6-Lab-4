#!/usr/bin/python3

import os
from PIL import Image


size = (600, 400)
src_dir = "/home/student/supplier-data/images/"
for file in os.listdir(src_dir):
    title, ext = os.path.splitext(file)
    infile = os.path.join(src_dir, title) + ".jpeg"
    try:
        with Image.open(src_dir + file) as im:
            im.convert("RGB").resize(size).save(infile)
    except OSError:
        print("cannot convert", file)
        