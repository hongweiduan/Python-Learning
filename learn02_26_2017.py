class cap_str(str):
	"""docstring for cap_str"""
	def __new__(cls,string):
		string = string.upper()
		return str.__new__(cls,string)
	def __init__(self, arg):
		super(cap_str, self).__init__()
		self.arg = arg
					
# print (cap_str("ssss"))

class C:
	def __init__(self):
		print("I'm the function of __init__(),I'm be called")
	def __del__(self):
		print("I'm the function of __del__(),I'm be called")
# c1 = C()
# c2 =c1
# c3 =c2

# del c2
# del c1
# del c3

class New_int(int):
	def __add__(self,other):
		return int.__sub__(self,other)
	def __sub__(self,other):
		return int.__add__(self,other)

# a = New_int(2)
# b =5
# print(a+b)

# print(b%a)
# print(divmod(b,a)) # get a tuples
value = 12
b = (value-32)/1.8
a = ('a %.2f' % b)
print a
_temp_C = int('%.2f' % (str((int(value)-32)/1.8)))