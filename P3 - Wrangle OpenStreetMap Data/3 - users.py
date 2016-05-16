# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 00:18:17 2015

Exploring users.

@author: galgoczg
"""

import xml.etree.ElementTree as ET


def get_user(element):
    return 
    
def process_map(filename):
    users = set()
    for _, element in ET.iterparse(filename):
        try:
            users.add(element.attrib['uid'])
        except KeyError:
            continue

    return users
    
users = process_map('dublin_ireland.osm')
print len(users)

"""
Results:
1053
"""