---
- hosts: vyos
  collections:
    - vyos.vyos
  gather_facts: yes
  tasks:
    - name: facts
      vyos_facts:
        gather_subset:
          - '!all'
          - '!min'
        gather_network_resources:
          - interfaces
