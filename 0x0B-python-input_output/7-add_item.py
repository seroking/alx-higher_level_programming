#!/usr/bin/python3
""" module : 7-add_item.py"""



from sys import argv

load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

filename = "add_items.json"

try:
    items = load_from_json_file(filename)
except FileNotFoundError:
    items = []

for i in range(0, len(argv)):
    items.append(argv[i])

save_to_json_file(items, filename)
