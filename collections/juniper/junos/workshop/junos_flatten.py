import json
import pyperclip

def getKeys(val, old="$"):
    if isinstance(val, dict):
        for k in val.keys():
            getKeys(val[k], old + "." + str(k))
    elif isinstance(val, list):
        for i, k in enumerate(val):
            getKeys(k, old + "." + str(i))
    else:
        print("{} : {}".format(old,str(val)))



data = {"diff": {
    "prepared": "[edit system]\n+   ntp {\n+       server 1.1.1.1 key 12; ## SECRET-DATA\n+       server 1.1.1.2;\n+       server 1.1.1.3 key 16 prefer; ## SECRET-DATA\n+       server 1.1.1.4 key 15; ## SECRET-DATA\n+   }"
}
}

def flatten_json(y):
    out = {}

    def flatten(x, name=''):
        if type(x) is dict:
            for a in x:
                flatten(x[a], name + a + '_')
        elif type(x) is list:
            i = 0
            for a in x:
                flatten(a, name + str(i) + '_')
                i += 1
        else:
            out[name[:-1]] = x

    flatten(y)
    return out


# filter1 = data["diff"]["prepared"]
#
# print(filter1)
# filter2 = filter1.split("\n+")
# print(filter2)
# filter3 = ' '.join([str(elem) for elem in filter2])
from pandas import json_normalize
json_normalize(data)
print("F3" + data["diff"]["prepared"])
print(data)
final_output = flatten_json(data)
print("Final_output", final_output)
final_output1 = flatten_json(final_output)
final_output1 = final_output1.split("\n+")
print("Final_output1", final_output1)
#getKeys(data)




























# data = json.loads(pyperclip.paste())

# default_callback_plugin =  {
#     "msg": "Syslog server check - This check has failed with the following output([edit system syslog]\n+    host 10.1.1.12 {\n+        any error;\n+    }\n[edit system syslog]\n     file test9 { ... }\n+    file qflogs {\n+        archive size 1g;\n+        structured-data {\n+            brief;\n+        }\n+    })"
# }



#
# filter1 = default_callback_plugin["msg"].split("\n+")
#
# print(filter1)
# filter2 = filter1.split("\n")
# for filter
# print(filter2)


