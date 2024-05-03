# about_REST_API

- A *REST API* HPE termékekben való használatának bemutatása. Maga a REST szó egy rövidítés, jelentése: **representational state transfer**, az API pedig: **application programming interface**. A REST API egy olyan, elsősorban gép-gép kommunikációra kitalált architektúra, amely laza szabályzással teszi lehetővé, hogy programok a HTTP/HTTPS protokolt használva jussanak információhoz vagy befolyásolják más programok működését. Laza szabályzás alatt azt kell érteni, hogy a REST API-nak nincs kötött előírása az URL-ekkel kapcsolatban. 

- A [*Redfish*](https://www.dmtf.org/standards/redfish) egy standard, mely egyszerű és biztonságos managementre terveztek konvergált, hybrid IT és software definiált datacenterek részére. A *Redfish* standard meghatározza az adatlekéréshez használható URL-eket és a visszakapott adatok formáját.

- A REST API kérések, vagy utasítások visszaadott eredménye általában valamilyen [JSON](https://www.json.org/json-en.html) formátumú adattömeg. A JSON betűszó a *JavaScript Object Notation* rövidítése és egy könnyen olvasható ám programok számára is könnyedén feldolgozható adatcsere-formátum.

## CuRL példák

Bár a REST API elsősorban gép-gép kapcsolatra lett tervezve, olykor előfordulhat, hogy arra van szükség, hogy azt program írása nélkül legyen használható. Ezért olyan rendszereken, melyeken a curl parancs elérhető, az alábbi módon lehet például a BIOS beállításokat lekérdezni. Mivel az iLO-k jelentős részében csak self-signed certificate található, szükség lesz a `-insecure` kapcsoló használatára, hogy annak ellenőrzésén a curl ne akadjon meg. A visszakapott, JSON formátumú eredményt a jq parancs fogja olvashatóra formázni.

    curl https://172.16.0.3/redfish/v1/systems/1/bios/settings/ --insecure -u hpadmin:HPinvent123 -L -s | jq

## PowerShell példák
(Microsoft PowerShell 7.0 vagy újabb szükséges. Ennek telepítése pl: `winget install --id Microsoft.PowerShell --source winget`)

PowerShellben a Invoke-RestMethod használható REST API hívásokra. Az alábbi példában a `-SkipCertificateCheck` paraméterrel lehet kikapcsolni a certificate ellnőrzést, ez fontos, ha az iLO-nak self-signed certificate-je van, ami általában a jellemző állapot. Mivel a kimenet itt is ömlesztett, mint a curl esetében, azt formázni kell a ConvertTo-Json metódussal:

    PS C:\Users\saabi> $Cred = Get-Credential
    
    PowerShell credential request
    Enter your credentials.
    User: hpadmin
    Password for user hpadmin: ***********
    
    PS C:\Users\saabi> $Params = @{
    >> Uri = "https://172.16.0.3/redfish/v1/systems/1/bios/settings"
    >> Authentication = "Basic"
    >> Credential = $Cred
    >> }
    PS C:\Users\saabi> Invoke-RestMethod @Params -SkipCertificateCheck | ConvertTo-Json

Bár nem REST API, azért megjegyzem, hogy nem feltétlen kell a nevet és a jelszót interaktívan bekérni. Ha scriptbe tennénk, akkor ez az eljárás:

    $myUser = "hpadmin"
    $myPass = "HPinvent123"
    $secPass = ConvertTo-SecureString $myPass -AsPlainText -Force
    $Cred = New-Object -TypeName System.Management.Automation.PSCredential -ArgumentList $myUser, $secPass

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

## ToDo
- CuRL példák
- PowerShell példák
- BIOS beállíás változtatás/átírás
- Firmware upgrade/downgrade
