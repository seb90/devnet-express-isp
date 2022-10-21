import meraki
import include

api = meraki.DashboardAPI(
    api_key=include.API_KEY,
    output_log=False,
    print_console=False

)

networks = api.organizations.getOrganizationNetworks(include.ORGANIZATION_ID)

# Wenn Tag auf dem Network:
for network in networks:  # über alle networks gehen
    if 'Firewall' in network['tags']:  # ist der tag enthalten?
        new_rules = []  # liste erstellen
        my_rule = {'comment': 'Sebastians Regel', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443', 'destCidr': '172.24.1.0/24', 'srcPort': 'Any', 'srcCidr': 'Any', 'syslogEnabled': False}
        new_rules.append(my_rule)  # regel zur liste hinzufügen

        firewall_rules = api.appliance.getNetworkApplianceFirewallL3FirewallRules(network['id'])  # aktuelle regeln auslesen
        for fw_rule in firewall_rules['rules']:  # über die regeln gehen
            if fw_rule['comment'] != 'Default rule':  # die default regel ignorieren, da die automatisch gesetzt wird.
                new_rules.append(fw_rule)  # regel zur liste hinzufügen

        response = api.appliance.updateNetworkApplianceFirewallL3FirewallRules(network['id'],rules=new_rules)  # neue liste einspielen
        print(response)  # ergebnis ausgeben


# Wenn Tag auf dem Device:
for network in networks:  # über alle networks gehen
    devices = api.networks.getNetworkDevices(network['id'])  # alle geräte im netzwerk auslesen
    for device in devices:  # über alle geräte gehen
        if 'Firewall' in device['tags']:  # ist der tag enthalten?
            new_rules = []  # liste erstellen
            my_rule = {'comment': 'Sebastians Regel', 'policy': 'allow', 'protocol': 'tcp', 'destPort': '443',
                       'destCidr': '172.24.1.0/24', 'srcPort': 'Any', 'srcCidr': 'Any', 'syslogEnabled': False}
            new_rules.append(my_rule)  # regel zur liste hinzufügen

            firewall_rules = api.appliance.getNetworkApplianceFirewallL3FirewallRules(
                network['id'])  # aktuelle regeln auslesen
            for fw_rule in firewall_rules['rules']:  # über die regeln gehen
                if fw_rule['comment'] != 'Default rule':  # die default regel ignorieren, da die automatisch gesetzt wird.
                    new_rules.append(fw_rule)  # regel zur liste hinzufügen

            response = api.appliance.updateNetworkApplianceFirewallL3FirewallRules(network['id'], rules=new_rules)  # neue liste einspielen
            print(response)  # ergebnis ausgeben

