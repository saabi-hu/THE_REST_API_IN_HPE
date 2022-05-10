#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
fwvers.py - Example program, how to query firmware versions from a HPE ProLiant Gen10(Plus) server
"""

import sys
import redfish


ILO_URL = "172.16.0.5"
ILO_LOGIN = "hpadmin"
ILO_PASSWORD = "HPinvent123"


ILO = redfish.RedfishClient(base_url=ILO_URL, username=ILO_LOGIN, password=ILO_PASSWORD)
ILO.login(auth="session")
RESPONSE = ILO.get("/redfish/v1/UpdateService/FirmwareInventory/")

for i in RESPONSE.dict['Members']:
    fwinventory = ILO.get(i['@odata.id'])
    name = fwinventory.dict['Name']
    version = fwinventory.dict['Version']
    sys.stdout.write("%s : %s : %s\n" % (i['@odata.id'], name, version))

#ILO.logout()