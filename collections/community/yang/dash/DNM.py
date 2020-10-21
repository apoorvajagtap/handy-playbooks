import json
import xml.etree.ElementTree as ET

data_dict = {
    "interface-configurations": {
        "-xmlns": "http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg",
        "interface-configuration": ""
    }
}

# convert python dict/object into appropriate json objects.
# write json string output to file
# json.dump()
# json module in Python module provides a method called dump(),
# which converts the Python objects into appropriate json objects.
# It is a slight variant of dumps() method
out_file = open("../filter/openconfig-interfaces.json", "w+")
json.dump(data_dict, out_file, indent=4)

# Load JSON data from file
# json.load() takes a file object and returns the json object.
# A JSON object contains data in the form of key/value pair.
# The keys are strings and the values are the JSON types.

with open("../filter/openconfig-interfaces.json", "r") as json_file:
    data = json.load(json_file)
print(data)
# Every xml file must have exactly one root element
# root = ET.Element("interface-configurations")
#
# Maths = ET.SubElement(root, "maths")