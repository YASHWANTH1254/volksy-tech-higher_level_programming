#!/usr/bin/python3
"""file added."""
from pathlib import Path
import sys
import json


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

args = []
if Path('add_item.json').exists():
    args = load_from_json_file('add_item.json')

for i in range(1, len(sys.argv)):
    args.append(str(sys.argv[i]))

save_to_json_file(args, 'add_item.json')
