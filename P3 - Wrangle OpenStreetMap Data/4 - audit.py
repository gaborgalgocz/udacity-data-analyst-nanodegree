# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:08:24 2015

Cleaning the data.

@author: galgoczg
"""

import xml.etree.cElementTree as ET
from collections import defaultdict
import re

osmfile = "dublin_ireland.osm"
street_type_re = re.compile(r'\b\S+\.?$', re.IGNORECASE)

#List of intially expected values
expected = ["Abbey", "Alley", "Avenue", "Castle", "Center", "Centre", "Chase", 
            "Close", "Cottages", "Court", "Crescent", "Cross", "Dale", "Downs", "Drive", "East", 
            "Estate", "Gardens", "Glade", "Glen", "Green", "Grove", "Hall", "Harbour",
            "Heath", "Heights", "Hill", "House", "Lane", "Lawn", "Lawns", "Lodge", "Lower", 
            "Manor", "Mall", "Market", "Meadow", "Meadows", "Mew", "Mews",
            "Mount", "North", "Oaks", "Parade", "Park", "Place", "Plaza", "Quay", "Residential", 
            "Rise", "Road", "Row", "South", "Street", "Square", "Terrace", "Upper", "Vale", "Valley", 
            "View", "Villa", "Village", "Villas", "Walk", "Way", "West", "Wood", "Woods",  ]

#List of approved values, that I encountered during the cleaning process
approved = ["Airport", "Albany","Alders", "Apartments", "Archerswood", "Ardglas", "Arundel", "Ashurst",
            "Avonmore", "Ballycoolin", "Bank", "Bar", "Barnacullia", "Bay", "Bayview", "Beeches", "Beechview",
            "Belfield", "Belmont", "Biscayne", "Blackpitts", "Blanchardstown", "Bohernabreena", 
            "Boulevard", "Brae", "Brambles", "Bridge", "Broadstone", "Brook", "Brookdene", 
            "Brookfield", "Brooklawn", "Brookside", "Brugh", "Buildings", "Bypass", "Cairn",
            "Cairnfort", "Campus", "Cappaghmore", "Carraiglea", "Carrigwood", "Castlebrook",
            "Castlelands", "Castletown", "Cedarmount", "Cedars", "Chapelton", "Cherries", "Cherrygarth",
            "Cherrywood", "Churchfields", "Churchlands", "Citywest", "Clanmawr", "Cliffs", 
            "Clonasleigh", "Coille", "College", "Complex", "Coolevin", "Coolkill", 
            "Coolnahinch", "Coolnevaun", "Coombe", "Copse", "Cornelscourt", "Corner", 
            "Cornmarket", "Courtyard", "Cove", "Crossing", "Crowfall", "Dales", "Daleview", 
            "Dalymount", "Demesne", "Dene", "District", "Dock", "Drumahill", "Dublin", "Ellesmere", 
            "Elmfield", "Elms", "End", "Extension", "Fairview", "Fairways", "Farm", 
            "Fernbrook", "Fitzpatrick", "Fleurville", "Fosterbrook", "Fosters", "Friarsland",
            "Garth", "Gate", "Gates", "Glasnevin", "Gleneaston", "Glenview", "Grange", 
            "Grangefield", "Great", "Greenlands", "Greygates", "Harvard", "Haven",
            "Hazelbrook", "Hazelwood", "Heathfield", "Hillcrest", "Holywell", "Innismore",
            "Island", "Janeville", "Kilbride", "Killegar", "Knocknagow", "Knocknashee",
            "Laraghcon", "Laurels", "Laurelton", "Laurleen", "Lehaunstown", "Leopardstown",
            "Little", "Littlewood", "Lorcan", "Lotts", "Louvain", "Maples", "Mara", "Mart",
            "Maryland", "Mayfield", "Mead", "Meadowbank", "Meadowfield", "Meath", "Middle",
            "Millstead", "Moorefield", "Moorings", "Moyville", "Newmarket", "Newtownsmith", "Norwood",
            "Oakdene", "Orchard", "Paddock", "Pakenham", "Parklands", "Parkvale",
            "Parkview", "Pimlico", "Pinar", "Pinehurst", "Pines", "Pinewood", "Pleasant",
            "Point", "Point", "Poplars", "Powerscourt", "Princeton", "Ralahine", "Ranelagh", 
            "Rathcoole", "Rectory","Rest", "Richmond", "Richview", "Rockbrook", "Rockfield", "Rocwood", 
            "Roseacre", "Rowanbyrn", "Rubrics", "Rushbrook", "Salamanca", "Sandford",
            "Seafield", "Seapark", "Shee", "Sloperton", "Slopes", "Smol", "Sommerville",
            "Sorbonne", "Southdene", "Stables", "Stoneybatter", "Strand", "Summerhill",
            "Sunnybank", "Sycamores", "Thicket", "Third", "Thorpe", "Torcaill", "Treesdale",
            "Ullardmor", "Vergemount", "Wansdowne", "Ward", "Weirview", "Wesbury",
            "Wilfield", "Willows", "Wingfield", "Woodlands", "Woodpark", "Woodside",
            "Woodview", "Yale", "Yard"
                ]

# Corrections
mapping = { "Rd.": "Road",
            "St": "Street",
            "lane": "Lane",
            "park": "Park",
            "residential": "Residential",
            "road": "Road",
            "street": "Street",
            "heights": "Heights",
            "Aspencourt": "Aspen Court",
            "Ave": "Avenue",
            "Avevnue": "Avenue",
            "Bervstede": "Berystede",
            "castletown": "Castletown",
            "Cente": "Center",
            "Donghmede": "Donaghmede",
            "Dundrum": "Dundrum",
            "Heidleberg": "Heidelberg",
             u"Mobhi\xa0Road": "Mobhi Road",
            "Nouth": "North",
            "Parknasilloge": "Parknasilla",
            "Roafd": "Road",
            "Sreet": "Street",
            "St": "Street",
            "1-9": "1-9",
            "10-21": "10-21",
            "26": "26",
            "14-28": "14-28",
            "27-31": "27-31",
            "32-39": "32-39",
            "4": "4",
            "40-44": "40-44",
            "48-": "48-",
            "1-13": "1-13"
                }

def audit_street_type(street_types, street_name):
    m = street_type_re.search(street_name)
    if m:
        street_type = m.group()
        if street_type not in expected + approved:
            street_types[street_type].add(street_name)


def is_street_name(elem):
    return (elem.attrib['k'] == "addr:street")


def audit(osmfile):
    osm_file = open(osmfile, "r")
    street_types = defaultdict(set)
    for event, elem in ET.iterparse(osm_file, events=("start",)):

        if elem.tag == "node" or elem.tag == "way":
            for tag in elem.iter("tag"):
                if is_street_name(tag):
                    audit_street_type(street_types, tag.attrib['v'])

    return street_types
            
def update_name(name, mapping):

    update = name.split(' ')
    last = update[-1]
    update[-1] = mapping[last]
    return ' '.join(update)


def test():
    st_types = audit(osmfile)
    #pprint.pprint(dict(st_types))

    for st_type, ways in st_types.iteritems():
        for name in ways:
            better_name = update_name(name, mapping)
            print name, "=>", better_name


if __name__ == '__main__':
    test()
            
