import xmltodict
import json

xml = '''<interface-configurations xmlns="http://cisco.com/ns/yang/Cisco-IOS-XR-ifmgr-cfg"><interface-configuration>
          </interface-configuration></interface-configurations>'''

my_dict = xmltodict.parse(xml)
json_data = json.dumps(my_dict)
print(json_data)
