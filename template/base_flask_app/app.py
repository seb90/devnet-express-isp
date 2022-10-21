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
    
    # Füge eigenen Python-Code um Daten abzufragen und zu modifizieren hier ein 
    
    return render_template('index.html', data_to_pass_to_the_html_page="")


#Funktionen
#(Optional) Füge eigene Funktionen hier ein


if __name__ == "__main__":
    app.run()