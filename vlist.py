import sys
from nimbleclient import NimOSClient
import pprint

Nimble_management_IP = "172.16.0.31"
Nimble_management_user = "admin"
Nimble_management_password = "admin"
pp = pprint.PrettyPrinter(indent=2)

NIMBLE = NimOSClient(Nimble_management_IP, Nimble_management_user, Nimble_management_password)


pp.pprint(NIMBLE.volumes.list())