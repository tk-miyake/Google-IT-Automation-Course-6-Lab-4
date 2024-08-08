#!/usr/bin/python3

import os
import requests


# txt_dir = "/home/student/supplier-data/descriptions/"
# img_dir = "/home/student/supplier-data/images/"

# for files in os.listdir(txt_dir):
#     with open(txt_dir + files, "r") as file:
#         lines = [line.strip() for line in file.readlines()]

#     key_lists = ["name", "weight", "description"]
#     dictionary = dict(zip(key_lists, lines))
    
#     for dicts in dictionary:
#         for keys in dicts:
#             dicts[keys] = int(dicts[keys])

#     response = requests.post("http://[external-IP-address]/fruits", data=description_data)
#     print("status_code", response.status_code)


txt_dir = "C:\\Users\\WS-ENG-MIYAKE\\txt\\"
# img_dir = "C:\\Users\\WS-ENG-MIYAKE\\"

for files in os.listdir(txt_dir):
    with open(txt_dir + files, "r") as file:
        lines = [line.strip() for line in file.readlines()]
        print(lines)




    # key_lists = ["name", "weight", "description"]
    # dictionary = dict(zip(key_lists, lines))
    # print(dictionary)
    
    # for dicts in dictionary:
        
    
    # for dicts in dictionary:
    #     for keys in dicts:
    #         dicts[keys] = int(dicts[keys])