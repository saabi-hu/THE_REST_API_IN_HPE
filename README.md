# about_REST_API
A REST API HPE termékekben való használatának bemutatása

## REST API dokumentációk
- [iLO RESTful API for HPE iLO 5 reference](https://hewlettpackard.github.io/ilo-rest-api-docs/ilo5/)
- [Python iLO Redfish Library docs](https://hewlettpackard.github.io/python-ilorest-library/)
- [HPE Nimble Storage SDK for Python doc](https://hpe-storage.github.io/nimble-python-sdk/)
- [HPE Nimble REST API Reference Version 5.1.1.0](https://infosight.hpe.com/InfoSight/media/cms/active/public/pubs_REST_API_Reference_NOS_51x.whz//index.html)
- [hpestorapi](https://hpestorapi.readthedocs.io/en/latest/)

## SDK-k
- [python-ilorest-library](https://github.com/HewlettPackard/python-ilorest-library)
- [HPE Nimble Storage SDK for Python](https://github.com/hpe-storage/nimble-python-sdk)
- [hpestorapi](https://github.com/HewlettPackard/python-storage-clients)

## CuRL példák

A BIOS verziójának lekérdezése:

    curl https://172.16.0.3/redfish/v1/UpdateService/FirmwareInventory/2/ --insecure -u hpadmin:HPinvent123 -L -s

És ennek formázatlan kimenete:

    {"@odata.context":"/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory","@odata.etag":"W/\"918DA6A4\"","@odata.id":"/redfish/v1/UpdateService/FirmwareInventory/2/","@odata.type":"#SoftwareInventory.v1_0_0.SoftwareInventory","Id":"2","Description":"SystemRomActive","Name":"System ROM","Oem":{"Hpe":{"@odata.context":"/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory","@odata.type":"#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory","DeviceClass":"aa148d2e-6e09-453e-bc6f-63baa5f5ccc4","DeviceContext":"System Board","Targets":["00000000-0000-0000-0000-000000000217","00000000-0000-0000-0000-000001413431"]}},"Status":{"Health":"OK","State":"Enabled"},"Version":"A41 v2.36 (03/09/2020)"}%

De a jq paranccsal olvasási szempontból kellemesre lehet formázni egy JSON kimenetet:

    {
      "@odata.context": "/redfish/v1/$metadata#SoftwareInventory.SoftwareInventory",
      "@odata.etag": "W/\"918DA6A4\"",
      "@odata.id": "/redfish/v1/UpdateService/FirmwareInventory/2/",
      "@odata.type": "#SoftwareInventory.v1_0_0.SoftwareInventory",
      "Id": "2",
      "Description": "SystemRomActive",
      "Name": "System ROM",
      "Oem": {
        "Hpe": {
          "@odata.context": "/redfish/v1/$metadata#HpeiLOSoftwareInventory.HpeiLOSoftwareInventory",
          "@odata.type": "#HpeiLOSoftwareInventory.v2_0_0.HpeiLOSoftwareInventory",
          "DeviceClass": "aa148d2e-6e09-453e-bc6f-63baa5f5ccc4",
          "DeviceContext": "System Board",
          "Targets": [
            "00000000-0000-0000-0000-000000000217",
            "00000000-0000-0000-0000-000001413431"
          ]
        }
      },
      "Status": {
        "Health": "OK",
        "State": "Enabled"
      },
      "Version": "A41 v2.36 (03/09/2020)"
    }


## PowerShell példák

## ToDo
- CuRL példák
- PowerShell példák
- BIOS beállíás változtatás/átírás
- Firmware upgrade/downgrade