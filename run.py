#!/usr/bin/python3

import os
import requests


src_dir = "/home/student/supplier-data/descriptions/"
url = "http://35.185.73.219/fruits/"

for files in os.listdir(src_dir):
    with open(src_dir + files, "r") as file:
        lines = file.readlines()
        name = lines[0].strip()
        weight = int(lines[1].strip().replace(" lbs", ""))
        description = lines[2].strip()
        image_name = files.split(".")[0] + ".jpeg"
        data = {"name": name, "weight": weight, "description": description, "image_name": image_name}

    response = requests.post(url, data=data)
    print("status_code", response.status_code)
