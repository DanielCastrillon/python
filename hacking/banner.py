import http.client

host = "10.0.2.255"
http = http.client.HTTPConnection(host, timeout=5)
http.request("HEAD", "")
server = http.getresponse().getheader('server')
vulnerables = open("vulnerables.txt", "r")
esVulnerable = False

for servicio in vulnerables:
	s = servicio.split(" ")
	if(s[0] in server):
		print(host,"tiene servicio", s[0],"con posible vulnerabilidad",s[1])
		esVulnerable = True
if(not esVulnerable):
	print(host,"no cuenta con un servicio vulnerable de la lista, o no da la informacion")