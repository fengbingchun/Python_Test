import colorama
import pickle

# Blog: https://blog.csdn.net/fengbingchun/article/details/141340532

def create_instance(cls, *args, **kwargs):  
	return cls(*args, **kwargs) 

class SpecialMethods(object):
	"""special methods of class"""

	'''initialization and destruction'''
	def __init__(self, data=[]):
		print(colorama.Fore.YELLOW + "call __init__ method")
		self.csdn = "https://blog.csdn.net/fengbingchun" # 这里会调用__setattr__ 
		self.github = "https://github.com/fengbingchun"
		self.data = data
		self.current = 0
		self.high = len(data)

	def __del__(self):
		print(colorama.Fore.YELLOW + "call __del__ method" + colorama.Style.RESET_ALL)

	def __new__(cls, *args, **kwargs):
		print(colorama.Fore.YELLOW + "call __new__ method")
		return super(SpecialMethods, cls).__new__(cls)
	
	def __init_subclass__(cls, **kwargs):
		print(colorama.Fore.YELLOW + "call __init_subclass__ method")
		super().__init_subclass__(**kwargs)
		print(f"subclass {cls.__name__} created")

	'''property access'''
	def __setattr__(self, name, value):
		print(colorama.Fore.YELLOW + "call __setattr__ method")
		self.__dict__[name] = value # 使用__dict__来避免无限递归

	def __getattr__(self, name):
		print(colorama.Fore.YELLOW + "call __getattr__ method")

		if name in self.__dict__:  
			return self.attributes[name]
		else:
			# raise ArithmeticError(f"'{type(self).__name__}' object has no attribute '{name}'")
			print(colorama.Fore.RED + f"'{type(self).__name__}' object has no attribute '{name}'")

	def __delattr__(self, name):
		print(colorama.Fore.YELLOW + "call __delattr__ method")

		if name in self.__dict__:
			super().__delattr__(name)
		else:
			print(colorama.Fore.RED + f"'{type(self).__name__}' object has no attribute '{name}'")

	# def __getattribute__(self, name):
	# 	print(colorama.Fore.YELLOW + "call __getattribute__ method")

	def __dir__(self):
		print(colorama.Fore.YELLOW + "call __dir__ method")
		default_dir = super().__dir__()

		modified_dir = [attr for attr in default_dir if attr != "_protected_method" and attr != "__private_method" ]
		return modified_dir
	
	def _protected_method(self):  
		print("call _protected_method method")

	def __private_method(self):  
		pass

	'''container methods'''
	def __len__(self):
		print(colorama.Fore.YELLOW + "call __len__ method")
		return len(self.__dict__)
	
	def __getitem__(self, index):
		print(colorama.Fore.YELLOW + "call __getitem__ method")
		return self.data[index]
	
	def __setitem__(self, index, value):
		print(colorama.Fore.YELLOW + "call __setitem__ method")
		self.data[index] = value

	def __delitem__(self, index):
		print(colorama.Fore.YELLOW + "call __delitem__ method")
		del self.data[index]
		self.high = len(self.data)

	def __iter__(self):
		print(colorama.Fore.YELLOW + "call __iter__ method")
		return self
	
	def __next__(self):
		print(colorama.Fore.YELLOW + "call __next__ method")
		if self.current >= self.high:
			raise StopIteration
		else:
			self.current += 1
			return self.data[self.current - 1]

	def __reversed__(self):
		print(colorama.Fore.YELLOW + "call __reversed__ method")
		return reversed(self.data)
	
	def __contains__(self, value):
		print(colorama.Fore.YELLOW + "call __contains__ method")
		return value in self.data
	
	'''numerical methods'''
	def __add__(self, other):
		print(colorama.Fore.YELLOW + "call __add__ method")
		if isinstance(other, SpecialMethods):
			return list(map(lambda x, y: x + y, self.data, other.data))
		elif isinstance(other, (int, float)):
			return [x + other for x in self.data]
		else:
			return NotImplemented
		
	def __radd__(self, other):
		print(colorama.Fore.YELLOW + "call __radd__ method")
		return self.__add__(other)
	
	def __sub__(self, other):
		print(colorama.Fore.YELLOW + "call __sub__ method")
		if isinstance(other, SpecialMethods):
			return list(map(lambda x, y: x - y, self.data, other.data))
		elif isinstance(other, (int, float)):
			return [x - other for x in self.data]
		else:
			return NotImplemented
		
	def __rsub__(self, other):
		print(colorama.Fore.YELLOW + "call __rsub__ method")
		return self.__sub__(other)		
	
	def __mul__(self, other):
		print(colorama.Fore.YELLOW + "call __mul__ method")
		return list(map(lambda x, y: x * y, self.data, other.data))
	
	def __truediv__(self, other):
		print(colorama.Fore.YELLOW + "call __truediv__ method")
		assert isinstance(other, (int, float))
		return [x / other for x in self.data]
	
	def __floordiv__(self, other):
		print(colorama.Fore.YELLOW + "call __floordiv__ method")
		assert isinstance(other, (int, float))
		return [x // other for x in self.data]
	
	def __pow__(self, other, modulo=None):
		print(colorama.Fore.YELLOW + "call __pow__ method")
		if modulo is not None:
			return [pow(x, other, modulo) for x in self.data]
		return [pow(x, other) for x in self.data]
	
	def __abs__(self):
		print(colorama.Fore.YELLOW + "call __abs__ method")
		return [abs(x) for x in self.data]
	
	def __neg__(self):
		print(colorama.Fore.YELLOW + "call __neg__ method")
		return [-x for x in self.data]
	
	def __pos__(self):
		print(colorama.Fore.YELLOW + "call __pos__ method")
		return self.data
	
	def __invert__(self):
		print(colorama.Fore.YELLOW + "call __invert__ method")
		return [~x for x in self.data]
	
	def __float__(self):
		print(colorama.Fore.YELLOW + "call __float__ method")
		return float(self.data[0])
	
	def __mod__(self, other):
		print(colorama.Fore.YELLOW + "call __mod__ method")
		return [x % other for x in self.data]
	
	def __divmod__(self, other):
		print(colorama.Fore.YELLOW + "call __divmod__ method")
		assert isinstance(other, (int, float))
		quotient, remainder = divmod(self.data[0], other)
		return quotient, remainder

	def __lshift__(self, other):
		print(colorama.Fore.YELLOW + "call __lshift__ method")
		return [x << other for x in self.data]
	
	def __rshift__(self, other):
		print(colorama.Fore.YELLOW + "call __rshift__ method")
		return [x >> other for x in self.data]
	
	def __and__(self, other):
		print(colorama.Fore.YELLOW + "call __and__ method")
		return [x & other for x in self.data]

	def __xor__(self, other):
		print(colorama.Fore.YELLOW + "call __xor__ method")
		return [x ^ other for x in self.data]
	
	def __or__(self, other):
		print(colorama.Fore.YELLOW + "call __or__ method")
		return [x | other for x in self.data]

	def __iadd__(self, other):
		print(colorama.Fore.YELLOW + "call __iadd__ method")
		self.data = [ x + other for x in self.data]
		return self
	
	def __isub__(self, other):
		print(colorama.Fore.YELLOW + "call __isub__ method")
		self.data = [x - other for x in self.data]
		return self

	'''string and sequence representation'''
	def __str__(self):
		print(colorama.Fore.YELLOW + "call __str__ method")
		return f"SpecialMethods class(csdn:{self.csdn}; github:{self.github})"
	
	def __repr__(self):
		print(colorama.Fore.YELLOW + "call __repr__ method")
		return f"SpecialMethods class(data:{self.data})"
	
	def __format__(self, format_spec):
		print(colorama.Fore.YELLOW + "call __format__ method")
		return format(str(self), format_spec)
	
	def __reduce__(self):
		print(colorama.Fore.YELLOW + "call __reduce__ method")
		return (create_instance, (SpecialMethods, self.data))
	
	def __bytes__(self):
		print(colorama.Fore.YELLOW + "call __bytes__ method")
		return str(self.data).encode("utf-8")	
	
	'''context management'''
	def __enter__(self):
		print(colorama.Fore.YELLOW + "call __enter__ method")
		return self
	
	def __exit__(self, exc_type, exc_val, exc_tb):
		print(colorama.Fore.YELLOW + "call __exit__ method")
		if exc_type is not None:
			print(f"Execution: {exc_type}:{exc_val}")

	'''comparison operators'''
	def __lt__(self, other):
		print(colorama.Fore.YELLOW + "call __lt__ method")
		if not isinstance(other, SpecialMethods):
			return NotImplemented
		return self.data[0] < other.data[0]
	
	def __le__(self, other):
		print(colorama.Fore.YELLOW + "call __le__ method")
		if not isinstance(other, SpecialMethods):
			return NotImplemented
		return self.data[0] <= other.data[0]

	def __eq__(self, other):
		print(colorama.Fore.YELLOW + "call __eq__ method")
		if not isinstance(other, SpecialMethods):
			return NotImplemented
		return self.data[0] == other.data[0]
	
	def __ne__(self, other):
		print(colorama.Fore.YELLOW + "call __ne__ method")
		return not self.__eq__(other)
	
	def __gt__(self, other):
		print(colorama.Fore.YELLOW + "call __gt__ method")
		if not isinstance(other, SpecialMethods):
			return NotImplemented
		return self.data[0] > other.data[0]

	def __ge__(self, other):
		print(colorama.Fore.YELLOW + "call __ge__ method")
		if not isinstance(other, SpecialMethods):
			return NotImplemented
		return self.data[0] >= other.data[0]
	
	def __bool__(self):
		print(colorama.Fore.YELLOW + "call __bool__ method")
		return self.data[0] != 0
	
	'''other'''
	def __hash__(self):
		print(colorama.Fore.YELLOW + "call __hash__ method")
		return hash(self.data[0])
	
	def __call__(self, *args, **kwargs):
		print(colorama.Fore.YELLOW + "call __call__ method")
		self._protected_method()

class SubClass(SpecialMethods):
	pass


if __name__ == "__main__":
	colorama.init(autoreset=True)

	# initialization and destruction
	methods1 = SpecialMethods()
	print("methods.special_attribute:", methods1.special_attribute)

	# property access
	del methods1.addr
	methods1.addr = "Tianjin"
	print("methods.addr:", methods1.addr)
	del methods1.addr

	print("dir:", dir(methods1))

	# container methods
	print("len:", len(methods1))

	methods2 = SpecialMethods([2, 4, 6, 8, 10])
	print("index3:", methods2[3])

	methods2[3] = -10
	print("indx3:", methods2[3])

	del methods2[3]
	print("index3:", methods2[3])

	for value in methods2:
		print("value:", value)

	for value in reversed(methods2):
		print("value:", value)

	print(5 in methods2)
	print(10 in methods2)

	# numerical methods
	print(methods2 + methods2)
	print(methods2 + 88)
	print(88 + methods2)
	print(methods2 - 88)
	print(88 - methods2)
	print(methods2 * methods2)
	print(methods2 / 2)
	print(methods2 // 2)
	print(methods2 ** 2)
	print(methods2 % 3)
	print(divmod(methods2, 2))
	print(methods2 << 2)
	print(methods2 >> 2)
	print(methods2 & 3)
	print(methods2 ^ 3)
	print(methods2 | 3)
	methods2 += 3
	print(methods2)
	methods2 -= 3
	print(methods2)

	methods3 = SpecialMethods([-2, 4, -6, 8, -10])
	print(abs(methods3))
	print(-methods3)
	print(+methods3)
	print(~methods3)
	print(float(methods3))

	# string and sequence representation
	print(str(methods3))
	print(repr(methods3))
	print(format(methods3))

	serialized = pickle.dumps(methods3)
	reconstructed = pickle.loads(serialized)
	print(reconstructed.data)

	print(bytes(methods2))

	# context management
	with methods3 as md3:
		print(md3)

	# comparison operators
	print(methods2 < methods3)
	print(methods2 <= methods3)
	print(methods2 == methods3)
	print(methods2 != methods3)
	print(methods2 > methods3)
	print(methods2 >= methods3)

	if methods2:
		print("methods2 is True")

	# other
	print(hash(methods2))
	print(hash(methods3))

	methods3()

	print("__class__:", methods3.__class__)
	print("__dict__:", methods3.__dict__)
	print("__doc__:", methods3.__doc__)
	print("__module__:", methods3.__module__)
	print("__name__:", SpecialMethods.__name__)

	print(colorama.Fore.GREEN + "====== test finish ======")
