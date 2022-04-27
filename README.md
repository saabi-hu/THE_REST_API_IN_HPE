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
(Microsoft PowerShell 7.0 vagy újabb szükséges. Ennek telepítése pl: winget install --id Microsoft.PowerShell --source winget)

PowerShellben a Invoke-RestMethod használható REST API hívásokra. Az alábbi példában a `-SkipCertificateCheck` paraméterrel lehet kikapcsolni a certificate ellnőrzést, ez fontos, ha az iLO-nak self-signed certificate-je van, ami általában a jellemző állapot. Az azonosításhoz használt `$Cred` változót a Get-Credential metódussal lehet beállítani: `$Cred = Get-Credential`.

    PS C:\Users\saabi> Invoke-RestMethod -SkipCertificateCheck -Uri "https://172.16.0.3/redfish/v1/systems/1/bios/settings/" -Authentication "Basic" -Credential $Cred

A formázatlan kimenet itt látható. 

    @odata.context    : /redfish/v1/$metadata#Bios.Bios
    @odata.etag       : W/"F72C63D114C6A4A4A4BCED1A626DC84F"
    @odata.id         : /redfish/v1/systems/1/bios/settings/
    @odata.type       : #Bios.v1_0_0.Bios
    AttributeRegistry : BiosAttributeRegistryA41.v1_2_36
    Attributes        : @{AcpiHpet=Enabled; AcpiRootBridgePxm=Enabled; AcpiSlit=Enabled; AdminEmail=; AdminName=; AdminOtherInfo=; AdminPhone=; AdvCrashDumpMode=Disabled; AmdL1Prefetcher=Enabled; AmdL2Prefetcher=
                        Enabled; AmdMemoryInterleaving=Auto; AmdSecureMemoryEncryption=Disabled; AmdSevNum=8; AsrStatus=Enabled; AsrTimeoutMinutes=Timeout10; AssetTagProtection=Unlocked; AutoPowerOn=RestoreLastSt
                        ate; BootMode=Uefi; BootOrderPolicy=RetryIndefinitely; CollabPowerControl=Disabled; ConsistentDevNaming=LomsAndSlots; CustomPostMessage=; DaylightSavingsTime=Disabled; Dhcpv4=Enabled; Dram
                        ControllerPowerDown=Disabled; DynamicPowerCapping=Disabled; EmbNicAspm=Disabled; EmbNicEnable=Auto; EmbNicLinkSpeed=Auto; EmbNicPCIeOptionROM=Enabled; EmbSas1Aspm=Disabled; EmbSas1Boot=Twe
                        ntyFourTargets; EmbSas1Enable=Auto; EmbSas1LinkSpeed=Auto; EmbSas1PcieOptionROM=Enabled; EmbSata1Aspm=Disabled; EmbSata1Enable=Auto; EmbSata1PCIeOptionROM=Enabled; EmbSata2Aspm=Disabled; E
                        mbSata2Enable=Auto; EmbSata2PCIeOptionROM=Enabled; EmbVideoConnection=Auto; EmbeddedDiagnostics=Enabled; EmbeddedSata=Ahci; EmbeddedSerialPort=Com2Irq3; EmbeddedUefiShell=Enabled; EmsConso
                        le=Disabled; EnabledCoresPerProc=0; EraseUserDefaults=No; ExtendedAmbientTemp=Disabled; ExtendedMemTest=Disabled; F11BootMenu=Enabled; FCScanPolicy=CardConfig; FanFailPolicy=Shutdown; FanI
                        nstallReq=EnableMessaging; FlexLom1Aspm=Disabled; FlexLom1Enable=Auto; FlexLom1LinkSpeed=Auto; FlexLom1PCIeOptionROM=Enabled; HttpSupport=Auto; IntelligentProvisioning=Enabled; InternalSDC
                        ardSlot=Enabled; Ipv4Address=0.0.0.0; Ipv4Gateway=0.0.0.0; Ipv4PrimaryDNS=0.0.0.0; Ipv4SecondaryDNS=0.0.0.0; Ipv4SubnetMask=0.0.0.0; Ipv6Address=::; Ipv6ConfigPolicy=Automatic; Ipv6Duid=Au
                        to; Ipv6Gateway=::; Ipv6PrimaryDNS=::; Ipv6SecondaryDNS=::; MaxMemBusFreqMHz=Auto; MaxPcieSpeed=PerPortCtrl; MemPatrolScrubbing=Enabled; MemRefreshRate=Refreshx1; MinProcIdlePower=C6; Mixe
                        dPowerSupplyReporting=Enabled; NetworkBootRetry=Enabled; NetworkBootRetryCount=20; NicBoot1=NetworkBoot; NicBoot2=Disabled; NicBoot3=Disabled; NicBoot4=Disabled; NicBoot5=NetworkBoot; NicB
                        oot6=Disabled; NumaGroupSizeOpt=Flat; NvmeOptionRom=Enabled; PciSlot1Aspm=Disabled; PciSlot1Bifurcation=Auto; PciSlot1Enable=Auto; PciSlot1LinkSpeed=Auto; PciSlot1OptionROM=Enabled; PciSlo
                        t2Bifurcation=Auto; PerformanceDeterminism=PerformanceDeterministic; PostBootProgress=Disabled; PostDiscoveryMode=Auto; PostF1Prompt=Delayed20Sec; PostVideoSupport=DisplayAll; PowerButton=
                        Enabled; PowerOnDelay=NoDelay; PowerRegulator=OsControl; PreBootNetwork=Auto; PrebootNetworkEnvPolicy=IPv4; PrebootNetworkProxy=; PreferredIOBus=0; PreferredIODevice=0; PreferredIOFunction
                        =0; ProcAMDBoost=Enabled; ProcAMDBoostControl=AmdFmaxBoostAuto; ProcAes=Enabled; ProcAmdFmax=0; ProcAmdIOMMU=Enabled; ProcAmdVirtualization=Enabled; ProcSMT=Enabled; ProductId=P04654-B21;
                        RedundantPowerSupply=BalancedMode; RemovableFlashBootSeq=ExternalKeysFirst; RestoreDefaults=No; RestoreManufacturingDefaults=No; RomSelection=CurrentRom; SataSecureErase=Disabled; SaveUser
                        Defaults=No; SecStartBackupImage=Disabled; SecureBootStatus=Disabled; SerialConsoleBaudRate=BaudRate115200; SerialConsoleEmulation=Vt100Plus; SerialConsolePort=Auto; SerialNumber=MXQ83704Z
                        G; ServerAssetTag=; ServerConfigLockStatus=Disabled; ServerName=esxi110.hpelab.local; ServerOtherInfo=; ServerPrimaryOs=; ServiceEmail=; ServiceName=; ServiceOtherInfo=; ServicePhone=; Set
                        upBrowserSelection=Auto; SpeculativeLockScheduling=Enabled; Sriov=Enabled; ThermalConfig=OptimalCooling; ThermalShutdown=Enabled; TimeFormat=Utc; TimeZone=Utc0; TpmChipId=None; TpmFips=Not
                        Specified; TpmState=NotPresent; TpmType=NoTpm; TransparentSecureMemoryEncryption=Disabled; UefiOptimizedBoot=Disabled; UefiSerialDebugLevel=Disabled; UefiShellBootOrder=Disabled; UefiShell
                        ScriptVerification=Disabled; UefiShellStartup=Disabled; UefiShellStartupLocation=Auto; UefiShellStartupUrl=; UefiShellStartupUrlFromDhcp=Disabled; UrlBootFile=; UrlBootFile2=; UrlBootFile3
                        =; UrlBootFile4=; UsbBoot=Enabled; UsbControl=UsbEnabled; UserDefaultsState=Disabled; UtilityLang=English; VirtualInstallDisk=Disabled; VirtualSerialPort=Com1Irq4; VlanControl=Disabled; Vl
                        anId=0; VlanPriority=0; WakeOnLan=Enabled; WorkloadProfile=GeneralPowerEfficientCompute; XGMIForceLinkWidth=Auto; XGMIMaxLinkWidth=Auto; iSCSIPolicy=SoftwareInitiator}
    Id                : settings
    Name              : BIOS Pending Settings

A JSON kimenet formázását a ConvertTo-Json metódus tudja elvégezni:

    PS C:\Users\saabi> Invoke-RestMethod -SkipCertificateCheck -Uri "https://172.16.0.3/redfish/v1/systems/1/bios/settings/" -Authentication "Basic" -Credential $Cred | ConvertTo-Json
    {
      "@odata.context": "/redfish/v1/$metadata#Bios.Bios",
      "@odata.etag": "W/\"F72C63D114C6A4A4A4BCED1A626DC84F\"",
      "@odata.id": "/redfish/v1/systems/1/bios/settings/",
      "@odata.type": "#Bios.v1_0_0.Bios",
      "AttributeRegistry": "BiosAttributeRegistryA41.v1_2_36",
      "Attributes": {
        "AcpiHpet": "Enabled",
        "AcpiRootBridgePxm": "Enabled",
        "AcpiSlit": "Enabled",
        "AdminEmail": "",
        "AdminName": "",
        "AdminOtherInfo": "",
        "AdminPhone": "",
        "AdvCrashDumpMode": "Disabled",
        "AmdL1Prefetcher": "Enabled",
        "AmdL2Prefetcher": "Enabled",
        "AmdMemoryInterleaving": "Auto",
        "AmdSecureMemoryEncryption": "Disabled",
        "AmdSevNum": 8,
        "AsrStatus": "Enabled",
        "AsrTimeoutMinutes": "Timeout10",
        "AssetTagProtection": "Unlocked",
        "AutoPowerOn": "RestoreLastState",
        "BootMode": "Uefi",
        "BootOrderPolicy": "RetryIndefinitely",
        "CollabPowerControl": "Disabled",
        "ConsistentDevNaming": "LomsAndSlots",
        "CustomPostMessage": "",
        "DaylightSavingsTime": "Disabled",
        "Dhcpv4": "Enabled",
        "DramControllerPowerDown": "Disabled",
        "DynamicPowerCapping": "Disabled",
        "EmbNicAspm": "Disabled",
        "EmbNicEnable": "Auto",
        "EmbNicLinkSpeed": "Auto",
        "EmbNicPCIeOptionROM": "Enabled",
        "EmbSas1Aspm": "Disabled",
        "EmbSas1Boot": "TwentyFourTargets",
        "EmbSas1Enable": "Auto",
        "EmbSas1LinkSpeed": "Auto",
        "EmbSas1PcieOptionROM": "Enabled",
        "EmbSata1Aspm": "Disabled",
        "EmbSata1Enable": "Auto",
        "EmbSata1PCIeOptionROM": "Enabled",
        "EmbSata2Aspm": "Disabled",
        "EmbSata2Enable": "Auto",
        "EmbSata2PCIeOptionROM": "Enabled",
        "EmbVideoConnection": "Auto",
        "EmbeddedDiagnostics": "Enabled",
        "EmbeddedSata": "Ahci",
        "EmbeddedSerialPort": "Com2Irq3",
        "EmbeddedUefiShell": "Enabled",
        "EmsConsole": "Disabled",
        "EnabledCoresPerProc": "0",
        "EraseUserDefaults": "No",
        "ExtendedAmbientTemp": "Disabled",
        "ExtendedMemTest": "Disabled",
        "F11BootMenu": "Enabled",
        "FCScanPolicy": "CardConfig",
        "FanFailPolicy": "Shutdown",
        "FanInstallReq": "EnableMessaging",
        "FlexLom1Aspm": "Disabled",
        "FlexLom1Enable": "Auto",
        "FlexLom1LinkSpeed": "Auto",
        "FlexLom1PCIeOptionROM": "Enabled",
        "HttpSupport": "Auto",
        "IntelligentProvisioning": "Enabled",
        "InternalSDCardSlot": "Enabled",
        "Ipv4Address": "0.0.0.0",
        "Ipv4Gateway": "0.0.0.0",
        "Ipv4PrimaryDNS": "0.0.0.0",
        "Ipv4SecondaryDNS": "0.0.0.0",
        "Ipv4SubnetMask": "0.0.0.0",
        "Ipv6Address": "::",
        "Ipv6ConfigPolicy": "Automatic",
        "Ipv6Duid": "Auto",
        "Ipv6Gateway": "::",
        "Ipv6PrimaryDNS": "::",
        "Ipv6SecondaryDNS": "::",
        "MaxMemBusFreqMHz": "Auto",
        "MaxPcieSpeed": "PerPortCtrl",
        "MemPatrolScrubbing": "Enabled",
        "MemRefreshRate": "Refreshx1",
        "MinProcIdlePower": "C6",
        "MixedPowerSupplyReporting": "Enabled",
        "NetworkBootRetry": "Enabled",
        "NetworkBootRetryCount": 20,
        "NicBoot1": "NetworkBoot",
        "NicBoot2": "Disabled",
        "NicBoot3": "Disabled",
        "NicBoot4": "Disabled",
        "NicBoot5": "NetworkBoot",
        "NicBoot6": "Disabled",
        "NumaGroupSizeOpt": "Flat",
        "NvmeOptionRom": "Enabled",
        "PciSlot1Aspm": "Disabled",
        "PciSlot1Bifurcation": "Auto",
        "PciSlot1Enable": "Auto",
        "PciSlot1LinkSpeed": "Auto",
        "PciSlot1OptionROM": "Enabled",
        "PciSlot2Bifurcation": "Auto",
        "PerformanceDeterminism": "PerformanceDeterministic",
        "PostBootProgress": "Disabled",
        "PostDiscoveryMode": "Auto",
        "PostF1Prompt": "Delayed20Sec",
        "PostVideoSupport": "DisplayAll",
        "PowerButton": "Enabled",
        "PowerOnDelay": "NoDelay",
        "PowerRegulator": "OsControl",
        "PreBootNetwork": "Auto",
        "PrebootNetworkEnvPolicy": "IPv4",
        "PrebootNetworkProxy": "",
        "PreferredIOBus": 0,
        "PreferredIODevice": 0,
        "PreferredIOFunction": 0,
        "ProcAMDBoost": "Enabled",
        "ProcAMDBoostControl": "AmdFmaxBoostAuto",
        "ProcAes": "Enabled",
        "ProcAmdFmax": 0,
        "ProcAmdIOMMU": "Enabled",
        "ProcAmdVirtualization": "Enabled",
        "ProcSMT": "Enabled",
        "ProductId": "P04654-B21",
        "RedundantPowerSupply": "BalancedMode",
        "RemovableFlashBootSeq": "ExternalKeysFirst",
        "RestoreDefaults": "No",
        "RestoreManufacturingDefaults": "No",
        "RomSelection": "CurrentRom",
        "SataSecureErase": "Disabled",
        "SaveUserDefaults": "No",
        "SecStartBackupImage": "Disabled",
        "SecureBootStatus": "Disabled",
        "SerialConsoleBaudRate": "BaudRate115200",
        "SerialConsoleEmulation": "Vt100Plus",
        "SerialConsolePort": "Auto",
        "SerialNumber": "MXQ83704ZG",
        "ServerAssetTag": "",
        "ServerConfigLockStatus": "Disabled",
        "ServerName": "esxi110.hpelab.local",
        "ServerOtherInfo": "",
        "ServerPrimaryOs": "",
        "ServiceEmail": "",
        "ServiceName": "",
        "ServiceOtherInfo": "",
        "ServicePhone": "",
        "SetupBrowserSelection": "Auto",
        "SpeculativeLockScheduling": "Enabled",
        "Sriov": "Enabled",
        "ThermalConfig": "OptimalCooling",
        "ThermalShutdown": "Enabled",
        "TimeFormat": "Utc",
        "TimeZone": "Utc0",
        "TpmChipId": "None",
        "TpmFips": "NotSpecified",
        "TpmState": "NotPresent",
        "TpmType": "NoTpm",
        "TransparentSecureMemoryEncryption": "Disabled",
        "UefiOptimizedBoot": "Disabled",
        "UefiSerialDebugLevel": "Disabled",
        "UefiShellBootOrder": "Disabled",
        "UefiShellScriptVerification": "Disabled",
        "UefiShellStartup": "Disabled",
        "UefiShellStartupLocation": "Auto",
        "UefiShellStartupUrl": "",
        "UefiShellStartupUrlFromDhcp": "Disabled",
        "UrlBootFile": "",
        "UrlBootFile2": "",
        "UrlBootFile3": "",
        "UrlBootFile4": "",
        "UsbBoot": "Enabled",
        "UsbControl": "UsbEnabled",
        "UserDefaultsState": "Disabled",
        "UtilityLang": "English",
        "VirtualInstallDisk": "Disabled",
        "VirtualSerialPort": "Com1Irq4",
        "VlanControl": "Disabled",
        "VlanId": 0,
        "VlanPriority": 0,
        "WakeOnLan": "Enabled",
        "WorkloadProfile": "GeneralPowerEfficientCompute",
        "XGMIForceLinkWidth": "Auto",
        "XGMIMaxLinkWidth": "Auto",
        "iSCSIPolicy": "SoftwareInitiator"
      },
      "Id": "settings",
      "Name": "BIOS Pending Settings"
    }

## ToDo
- CuRL példák
- PowerShell példák
- BIOS beállíás változtatás/átírás
- Firmware upgrade/downgrade