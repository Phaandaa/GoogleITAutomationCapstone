#!/usr/bin/env python3
import psutil
import shutil
import emails
import socket
import os


sender = "automation@example.com"
receiver = "{}@example.com".format(os.environ.get('USER'))
body = "Please check your system and resolve the issue as soon as possible."


cpu_usage = psutil.cpu_percent(interval=1)
if cpu_usage > 80:
    subject = "Error - CPU usage is over 80%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

disk_usage = shutil.disk_usage("/")
available_space_percent = (disk_usage.free / disk_usage.total) * 100
if available_space_percent < 20:
    subject = "Error - Available disk space is less than 20%"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)

available_memory = psutil.virtual_memory().available
if available_memory < 500*1024*1024:
    subject = "Error - Available memory is less than 500MB"
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)


resolved_ip = socket.gethostbyname("localhost")
if resolved_ip != "127.0.0.1":
    subject = "Error - Hostname 'localhost' is not resolved to '127.0.0.1'."
    message = emails.generate_error_email(sender, receiver, subject, body)
    emails.send_email(message)