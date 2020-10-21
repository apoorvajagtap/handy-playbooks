# have = [{'name': 'GigabitEthernet0/0/0/0'},
#  {'l2protocol': [{'cdp': 'forward'}, {'pvst': 'tunnel'}],
#   'l2transport': True,
#   'name': 'GigabitEthernet0/0/0/1',
#   'native_vlan': 10,
#   'propagate': True},
#  {'name': 'GigabitEthernet0/0/0/3'},
#  {'name': 'GigabitEthernet0/0/0/3.900', 'q_vlan': [20, 40]},
#  {'name': 'GigabitEthernet0/0/0/4', 'native_vlan': 40}]
#
# want = [{'l2protocol': [{'cdp': 'forward', 'pvst': None, 'stp': None, 'vtp': None},
#                  {'cdp': None, 'pvst': 'tunnel', 'stp': None, 'vtp': None}],
#   'l2transport': True,
#   'name': 'GigabitEthernet0/0/0/1',
#   'native_vlan': 10,
#   'propagate': True,
#   'q_vlan': None},
#  {'l2protocol': None,
#   'l2transport': None,
#   'name': 'GigabitEthernet0/0/0/3.900',
#   'native_vlan': 10,
#   'propagate': None,
#   'q_vlan': [20, 40]},
#  {'l2protocol': None,
#   'l2transport': None,
#   'name': 'GigabitEthernet0/0/0/4',
#   'native_vlan': 40,
#   'propagate': None,
#   'q_vlan': None}]
#
#
# interface = {'l2protocol': [{'cdp': 'forward', 'pvst': None, 'stp': None, 'vtp': None},
#                             {'cdp': None, 'pvst': 'tunnel', 'stp': None, 'vtp': None}],
#              'l2transport': True,
#              'name': 'GigabitEthernet0/0/0/1',
#              'native_vlan': 10,
#              'propagate': True,
#              'q_vlan': None}
#
# each = {'l2protocol': [{'cdp': 'forward'}, {'pvst': 'tunnel'}],
#         'l2transport': True,
#         'name': 'GigabitEthernet0/0/0/1',
#         'native_vlan': 10,
#         'propagate': True}
# have_dict = {'l2protocol': [{'cdp': 'forward', 'pvst': None, 'stp': None, 'vtp': None},
#                             {'cdp': None, 'pvst': 'tunnel', 'stp': None, 'vtp': None}],
#              'name': 'GigabitEthernet0/0/0/1',
#              'q_vlan': None}
# commands=['interface GigabitEthernet0/0/0/1', 'no l2transport']
#
#
# # set_config
# want  = {'l2protocol': [{'cdp': 'forward', 'pvst': None, 'stp': None, 'vtp': None},
#                         {'cdp': None, 'pvst': 'tunnel', 'stp': None, 'vtp': None}],
#          'l2transport': True,
#          'name': 'GigabitEthernet0/0/0/1',
#          'native_vlan': 10,
#          'propagate': True,
#          'q_vlan': None}
# have = {'l2protocol': [{'cdp': 'forward'}, {'pvst': 'tunnel'}],
#         'l2transport': True,
#         'name': 'GigabitEthernet0/0/0/1',
#         'native_vlan': 10,
#         'propagate': True}
#
# diff = {('l2protocol',
#   ((('cdp', 'forward'), ('pvst', None), ('stp', None), ('vtp', None)),
#    (('pvst', 'tunnel'), ('cdp', None), ('stp', None), ('vtp', None))))}
#
#
# want = {'l2protocol': [{'cdp': 'forward', 'pvst': 'tunnel', 'stp': None, 'vtp': None}],
#  'l2transport': True,
#  'name': 'GigabitEthernet0/0/0/1',
#  'native_vlan': 10,
#  'propagate': True,
#  'q_vlan': None}
# have =  {'l2protocol': [{'cdp': 'forward'}, {'pvst': 'tunnel'}],
#          'l2transport': True,
#          'name': 'GigabitEthernet0/0/0/1',
#          'native_vlan': 10,
#          'propagate': True}
#
#
# def filter_dict_having_none_value(want, have):
#     # Generate dict with have dict value which is None in want dict
#     test_dict = dict()
#     test_key_dict = dict()
#     name = want.get("name")
#     if name:
#         test_dict["name"] = name
#     diff_ip = False
#     want_ip = ""
#     q(want)
#     q(have)
#     for k, v in iteritems(want):
#         if isinstance(v, dict):
#             for key, value in iteritems(v):
#                 if value is None and k in have and key in have.get(k):
#                     dict_val = have.get(k).get(key)
#                     test_key_dict.update({key: dict_val})
#                 test_dict.update({k: test_key_dict})
#         if isinstance(v, list) and isinstance(v[0], dict):
#             for key, value in iteritems(v[0]):
#                 if value is None and k in have and key in have.get(k):
#                     dict_val = have.get(k).get(key)
#                     test_key_dict.update({key: dict_val})
#                 test_dict.update({k: test_key_dict})
#             # below conditions checks are added to check if
#             # secondary IP is configured, if yes then delete
#             # the already configured IP if want and have IP
#             # is different else if it's same no need to delete
#             for each in v:
#                 if each.get("secondary"):
#                     want_ip = each.get("address").split("/")
#                     have_ip = have.get("ipv4")
#                     for each in have_ip:
#                         if len(want_ip) > 1 and each.get("secondary"):
#                             have_ip = each.get("address").split(" ")[0]
#                             if have_ip != want_ip[0]:
#                                 diff_ip = True
#                     if each.get("secondary") and diff_ip is True:
#                         test_key_dict.update({"secondary": True})
#                     test_dict.update({"ipv4": test_key_dict})
#                 # Checks if want doesn't have secondary IP but have has secondary IP set
#                 elif have.get("ipv4"):
#                     if [
#                         True
#                         for each_have in have.get("ipv4")
#                         if "secondary" in each_have
#                     ]:
#                         test_dict.update({"ipv4": {"secondary": True}})
#         if k == "l2protocol":
#             q(want[k])
#             q()
#             if want[k] != have.get("l2protocol") and have.get("l2protocol"):
#                 test_dict.update({k: v})
#         if v is None:
#             val = have.get(k)
#             test_dict.update({k: val})
#     return test_dict

want = ["{'cdp': 'forward'}", "{'pvst': 'tunnel'}"]
have = ["{'cdp': 'forward'}", "{'pvst': 'tunnel'}"]

diff = True

if have:
    if want:
        for h in have:
            for w in want:
                if h == w:
                    diff = False

            if not diff:
                break
    else:
        diff = True



# if have:
#     if want:
#         for h in have:
#             for w in want:
#                 dict_diff = {k: w[k] for k in set(w) - set(h)}
#                 if dict_diff:
#                     dict_diff = {k: v for k, v in dict_diff.items() if v is not None}
#                 if dict_diff:
#                     diff = True
#                     break
#             if diff:
#                 break


print(diff)
