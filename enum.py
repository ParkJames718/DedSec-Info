import dns.resolver
from dns.exception import DNSException
dominio = "vipprint.com.br"
registros = ["A", "AAAA", "MX", "NS", "CNAME", "PTR", "CERT", "SRV", "TXT", "SOA", "HINFO", "AFSDB", "NAPTR", "LOC"]
for registro in registros:
	try:
		resposta = dns.resolver.resolve(dominio, registro, raise_on_no_answer=False)
		resposta.lifetime = 1.0
		if resposta.rrset is not None:
			print (resposta.rrset)
	except DNSException:
		pass
