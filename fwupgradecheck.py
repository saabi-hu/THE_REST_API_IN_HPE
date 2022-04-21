import redfish
import sys


default_ilo_login = "hpadmin"
default_ilo_password = "HPinvent123"
iLO_IPs = ["172.16.0.3","172.16.0.4","172.16.0.5","172.16.0.6","172.16.0.7","172.16.0.8"]

# Collects BIOS versions from the specified servers and verifies that an update is required. 
for IP in iLO_IPs:
    iLO = redfish.RedfishClient(base_url=IP, username=default_ilo_login, password=default_ilo_password)
    iLO.login(auth="session")
    response = iLO.get("/redfish/v1/UpdateService/FirmwareInventory/2/") # second item contains the BIOS version
    bios_version = response.dict["Version"].split()[1] # cut off the HW version and the date
    sys.stdout.write("%s: System ROM: %s" % (IP, bios_version))
    if float(bios_version[1:]) < 2.40:
        sys.stdout.write("   !!!  Needs BIOS upgrade  !!!\n")
    else:
        sys.stdout.write("\n")