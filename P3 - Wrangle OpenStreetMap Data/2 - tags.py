# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 00:04:25 2015

Checking the tags.

@author: galgoczg
"""

import xml.etree.cElementTree as ET
import pprint
import re

lower = re.compile(r'^([a-z]|_)*$')
lower_colon = re.compile(r'^([a-z]|_)*:([a-z]|_)*$')
problemchars = re.compile(r'[=\+/&<>;\'"\?%#$@\,\. \t\r\n]')


def key_type(element, keys):
    if element.tag == "tag":
        k_value = element.attrib['k']
        if lower.search(k_value) is not None:
            keys['lower'] += 1
        elif lower_colon.search(k_value) is not None:
            keys['lower_colon'] += 1
        elif problemchars.search(k_value) is not None:
            keys["problemchars"] += 1
            print element.attrib['k']
        else:
            keys['other'] += 1

    return keys


def process_map(filename):
    keys = {"lower": 0, "lower_colon": 0, "problemchars": 0, "other": 0}
    for _, element in ET.iterparse(filename):
        keys = key_type(element, keys)

    return keys


keys = process_map('dublin_ireland.osm')
pprint.pprint(keys)

"""
Result: 
{'lower': 441471, 'lower_colon': 239972, 'other': 30876, 'problemchars': 0}
"""
