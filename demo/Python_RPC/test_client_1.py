import xmlrpc.client

s = xmlrpc.client.ServerProxy("http://localhost:8000")
print("sum:", s.add(2, 3))

