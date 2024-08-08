#!/usr/bin/python3


import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module

url = "http://localhost/upload/"
img_dir = "/home/student/supplier-data/images/"

for file in os.listdir(img_dir):
    title, ext = os.path.splitext(file)
    
    if ext == ".jpeg":
        try:
            with open(img_dir + file, 'rb') as opened:
                r = requests.post(url, files={'file': opened})
        except OSError:
            print("cannot open", file)
