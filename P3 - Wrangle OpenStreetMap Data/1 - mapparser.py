# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 23:09:41 2015

Counting the tags in the OSM file.

@author: galgoczg
"""

import xml.etree.cElementTree as ET
import pprint
from collections import defaultdict

def count_tags(filename):
    counts = defaultdict(int)
    for line in ET.iterparse(filename):
        current = line[1].tag
        counts[current] += 1
    return counts
    
tags = count_tags('dublin_ireland.osm')
pprint.pprint(tags)

"""
Results: 

defaultdict(<type 'int'>, {'node': 1013127, 'nd': 1369262, 'bounds': 1, 'member': 42952, 
'tag': 712319, 'relation': 2736, 'way': 176115, 'osm': 1})

"""