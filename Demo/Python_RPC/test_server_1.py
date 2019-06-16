from xmlrpc.server import SimpleXMLRPCServer

# Blog: https://blog.csdn.net/fengbingchun/article/details/92406377

class MyFuncs:
	def add(self, a, b):
		return a + b

if __name__ == "__main__":
	s = SimpleXMLRPCServer(("localhost", 8000))
	s.register_instance(MyFuncs())
	print("server is online ...")
	s.serve_forever()

