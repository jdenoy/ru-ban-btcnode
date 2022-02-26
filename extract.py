#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import requests
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
import json

bitnode_data_url = "https://bitnodes.io/api/v1/snapshots/latest/"

bitnoderesponse = requests.get(bitnode_data_url, verify=False)
for nodeentry in bitnoderesponse.json()['nodes'].items():
    if nodeentry[1][7] is not None:
        if "RU" in nodeentry[1][7] :
            if "]:" in nodeentry[0]:
                print(nodeentry[0][1:nodeentry[0].find("]:")]+"/128")
            else:
                print(nodeentry[0][0:nodeentry[0].find(":")]+"/32")
