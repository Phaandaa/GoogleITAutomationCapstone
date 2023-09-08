#!/usr/bin/env python3
import requests
import os

# This example shows how a file can be uploaded using
# The Python Requests module
url = "http://localhost/upload/"
folder_path = "./supplier-data/images"
file_list = os.listdir(folder_path)
for filename in file_list:
        if filename.lower().endswith('.jpeg'):
            file_path = os.path.join(folder_path, filename)
            print(file_path)
            with open(file_path, 'rb') as opened:
                r = requests.post(url, files={'file': opened})

