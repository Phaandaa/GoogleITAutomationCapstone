#!/usr/bin/env python3
import os
import reports
import emails
from datetime import date
import sys

def populate_data():
    fruits = []
    folder_path = "./supplier-data/descriptions"
    file_list = os.listdir(folder_path)
    print(file_list)
    for txt_file in file_list:
        with open(os.path.join(folder_path, txt_file), 'r') as review:
            content_placeholder = []
            placeholder_dict = {}
            for line in review:
                line = line.rstrip()
                content_placeholder.append(line)
            placeholder_dict["name"] = content_placeholder[0]
            placeholder_dict["weight"] = content_placeholder[1]
        fruits.append(placeholder_dict)
        print(fruits)
    return fruits


def main(argv):
    today = date.today()
    title = f"Processed Update on {today}"
    data = populate_data()
    text = ''
    for fruit in data:
        text += f"name: {fruit['name']}<br/>weight: {fruit['weight']}<br/><br/>"
    text.rstrip("<br/>")
    reports.generate("/tmp/processed.pdf", title, text)

    sender = "automation@example.com"
    receiver = "{}@example.com".format(os.environ.get('USER'))
    subject = "Upload Completed - Online Fruit Store"
    body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
    message = emails.generate_email(sender, receiver, subject, body, "/tmp/processed.pdf")
    emails.send_email(message)



if __name__ == "__main__":
    main(sys.argv)