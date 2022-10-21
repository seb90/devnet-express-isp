"""
Flask Aufgabe 

Aufgabe: Ausgabe aller Geräte aus dem Inventory auf einer Website
Zusatz: Einbinden der Sensorendaten (Temperatur und Luftfeuchte) auf der Website"

Hilfreiche Ressourcen:
* Meraki Dashboard API Dokumentation: https://developer.cisco.com/meraki/api-latest/
* Repository zum Meraki SDK: https://github.com/meraki/dashboard-api-python
* HTML Tutorial: https://www.w3schools.com/html/
* Jinja Template Dokumentation: https://jinja.palletsprojects.com/en/2.9.x/templates/ 
* CSS Tutorial: https://www.w3schools.com/css/
"""

from flask import Flask, render_template
import meraki


#Globale Variablen
app = Flask(__name__)

DASHBOARD = meraki.DashboardAPI(
        api_key= 'Add your Meraki API here',
        base_url='https://api.meraki.com/api/v1/'
        )

#Routen
@app.route('/', methods=['GET'])
def index():

    #Liste als Speicher für alle Organisationen mit Inventar- und Sensordaten (Zusatz)
    all_data = []

    #Frage alle Organisationen zu einem API Key via API ab: https://developer.cisco.com/meraki/api-v1/#!get-organizations
    organizations = DASHBOARD.organizations.getOrganizations()

    #Für jede Organisation:
    for orga in organizations:

        #Lese die Organisations-ID aus
        organizationId = orga['id']

        #Erstelle ein Dictionary basierend auf dem orga Dictionary und den Inventardaten
        enhanced_organisation_data = add_inventory_data_to_orga_dict(organizationId, orga)

        #Zusatzaufgabe: Einbinden der Sensorendaten (Temperatur und Luftfeuchte) auf der Website"
        #Erstelle ein Dictionary basierend auf dem enhanced_organisation_data Dictionary und den Sensordaten
        enhanced_organisation_data = add_sensor_data_to_orga_dict(organizationId, enhanced_organisation_data)
        #Zusatz Ende

        #Füge das enhanced_organisation_data in die all_data Liste ein
        all_data.append(enhanced_organisation_data)

    return render_template('index.html', all_data=all_data)


#Funktionen
def add_inventory_data_to_orga_dict(organizationId, organization_data):
    '''
    Funktion erwartet die Organisations-ID und Daten (als Dictionary) und erweitert die genannten Daten um die Inventarinformation der Organisation
    '''

    #Frage die Inventargeräte für die Organization per API ab: https://developer.cisco.com/meraki/api-v1/#!get-organization-inventory-devices
    orga_inventory_devices = DASHBOARD.organizations.getOrganizationInventoryDevices(organizationId)

    #Füge die Inventardaten zu den Organisationsdaten hinzu
    organization_data['inventory_devices'] = orga_inventory_devices

    return organization_data


#Zusatzaufgabe: Einbinden der Sensorendaten (Temperatur und Luftfeuchte) auf der Website"
def add_sensor_data_to_orga_dict(organizationId, organization_data):
    '''
    Funktion erwartet die Organisations-ID und Daten (als Dictionary) und erweitert die genannten Daten um die Temperatur- und Feutigkeits-Sensordaten der Organisation
    '''

    #Festlegen der Metrik für die Sensordatenabfrage
    metrics=["humidity", "temperature"]

    #Frage die neusten Feuchtigkeits- und Temperatursensordaten für die Organization per API ab: https://developer.cisco.com/meraki/api-v1/#!get-organization-sensor-readings-latest
    orga_sensor_data = DASHBOARD.sensor.getOrganizationSensorReadingsLatest(organizationId, metrics=metrics)

    #Füge die Sensordaten zu den Organisationsdaten hinzu
    organization_data['latest_sensor_data'] = orga_sensor_data

    return organization_data
#Zusatz Ende


if __name__ == "__main__":
    app.run()