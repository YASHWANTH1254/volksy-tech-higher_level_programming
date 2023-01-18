#!/usr/bin/python3
"""6-load_from_json_file Module"""
import json


def load_from_json_file(filename):
    """load the string"""
    with open(filename, mode='r', encoding='utf-8') as f:
        return json.load(f)
