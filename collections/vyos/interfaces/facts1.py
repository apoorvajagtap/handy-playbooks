---
- hosts: vyos
  collections:
    - vyos.vyos
  gather_facts: no
  tasks:
    - name: vyos_facts
      vyos_facts:
       gather_subset:
         - default
       gather_network_resources:
         - ospfv2

