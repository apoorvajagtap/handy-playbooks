default_callback_plugin =  {
    "msg": "Syslog server check - This check has failed with the following output([edit system syslog]\n+    host 10.1.1.12 {\n+        any error;\n+    }\n[edit system syslog]\n     file test9 { ... }\n+    file qflogs {\n+        archive size 1g;\n+        structured-data {\n+            brief;\n+        }\n+    })"
}

# from pandas.io.json._normalize import nested_to_record

def flatten(d):
    out = {}
    for key, val in d.items():
        if isinstance(val, dict):
            val = [val]
        if isinstance(val, list):
            for subdict in val:
                if isinstance(val, list):
                    for item in val:
                        if isinstance(item, list) or isinstance(item, dict):
                            deeper = flatten(subdict).items()
                            out.update({key + ' ' + key2: val2 for key2, val2 in deeper})
        else:
            out[key] = val
    return out


my_dict = {'a': 1,
           'c': {'a': 2, 'b': {'x': 5, 'y': 10}},
           'd': [1, 2, 3]}

my_dict = {
           "areas": [
               {
                   "area_id": "2",
                   "area_type": {
                       "normal": True
                   },
                   "authentication": "plaintext-password",
                   "shortcut": "enable"
               },
               {
                   "area_id": "3",
                   "area_type": {
                       "nssa": {
                           "set": True
                       }
                   }
               },
               {
                   "area_id": "4",
                   "area_type": {
                       "stub": {
                           "default_cost": 20,
                           "set": True
                       }
                   },
                   "network": [
                       {
                           "address": "192.0.2.0/24"
                       }
                   ],
                   "range": [
                       {
                           "address": "192.0.3.0/24",
                           "cost": 10
                       },
                       {
                           "address": "192.0.4.0/24",
                           "cost": 12
                       }
                   ]
               }
           ],
           "auto_cost": {
               "reference_bandwidth": 2
           },
           "default_information": {
               "originate": {
                   "always": True,
                   "metric": 10,
                   "metric_type": 2,
                   "route_map": "ingress"
               }
           },
           "log_adjacency_changes": "detail",
           "max_metric": {
               "router_lsa": {
                   "administrative": True,
                   "on_shutdown": 10,
                   "on_startup": 10
               }
           },
           "mpls_te": {
               "enabled": True,
               "router_address": "192.0.11.11"
           },
           "neighbor": [
               {
                   "neighbor_id": "192.0.11.12",
                   "poll_interval": 10,
                   "priority": 2
               }
           ],
           "parameters": {
               "abr_type": "cisco",
               "opaque_lsa": True,
               "rfc1583_compatibility": True,
               "router_id": "192.0.1.1"
           },
           "passive_interface": [
               "eth2",
               "eth1"
           ],
           "redistribute": [
               {
                   "metric": 10,
                   "metric_type": 2,
                   "route_type": "bgp"
               }
           ]
       }

# flat = nested_to_record(my_dict, sep='_')
flat =  flatten(my_dict)
print(flat)

flat_commands = []
for key, val in flat.items():
    cmd = key + ' ' + str(val)
    flat_commands.append(cmd)

print(flat_commands)
