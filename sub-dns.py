import socket
domini = "vipprint.com.br"
with open("/usr/share/dnsrecon/subdomains-top1mil-20000.txt") as arquivo:
	nomes = arquivo.readlines()
for nome in nomes:
	DNS = nome.strip("\n")+"."+domini
	try:
		print(DNS+": "+socket.gethostbyname(DNS))
	except socket.gaierror:
		pass
