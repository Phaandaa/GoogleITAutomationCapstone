#! /usr/bin/env python3

import os
import requests
folder_path = "./supplier-data/descriptions"

file_list = os.listdir(folder_path)
print(file_list)
for txt_file in file_list:
    fruit_dict = {}
    content_placeholder = []
    with open(os.path.join(folder_path, txt_file), 'r') as review:
        for line in review:
            line = line.rstrip()
            content_placeholder.append(line)
    fruit_dict['name'] = content_placeholder[0]
    fruit_dict['weight'] = int(content_placeholder[1].split()[0])
    fruit_dict['description'] = content_placeholder[2]
    fruit_dict['image_name'] = os.path.splitext(txt_file)[0] + ".jpeg"

    print(fruit_dict)

    response = requests.post("http://34.125.128.129/fruits/", data=fruit_dict)
    print(response.status_code)