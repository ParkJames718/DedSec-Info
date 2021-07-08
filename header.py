# -*- coding: utf-8 -*-
import shodan
import sys
import requests

SHODAN_API_KEY = "UAPlyNLTy0HAfUKaXIbh7imWiiya8bGf"
api = shodan.Shodan(SHODAN_API_KEY)

target = (sys.argv[1])

dnsResolve = ('https://api.shodan.io/dns/resolve?hostnames=' + target + '&key=' + SHODAN_API_KEY)

resolved = requests.get(dnsResolve)
hostIP = resolved.json()[target]
host = api.host(hostIP)

print ("""IP: {}
Organização: {}
Sistema Operacional: {}
ISP: {}
""".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a'), host['isp']))

print("""País: {} {}
Cidade: {}
Latitude: {}
Longitude: {}
ASN: {}
Domínios: {}
""".format(host['country_name'], host['country_code'], host['city'], host['latitude'], host['longitude'], host['asn'], host['domains']))

for item in host['data']:
	print("""Porta: {}
	Banner: {}""".format(item['port'], item['data']))
