#!/usr/bin/python3
""" 5-save_to_json_file Module """
import json


def save_to_json_file(my_obj, filename):
    """save the python file"""
    with open(filename, mode='w', encoding='utf-8') as f:
        json.dump(my_obj, f)
