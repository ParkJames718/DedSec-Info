import requests
resposta = requests.head("https://vipprint.com.br")
for cabecalho,conteudo in resposta.headers.iteritems():
	print (cabecalho,":",conteudo)
