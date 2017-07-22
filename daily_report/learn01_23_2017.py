__metaclass__ = type
class Person(object):
	"""docstring for Person"""
	# def __init__(self, arg):
	# 	super(Person, self).__init__()
	# 	self.arg = arg

	def setName(self,name):
		self.name = name

	def getName(self):
		return self.name 

	def greet(self):
		print "Hello, world! I'm %s." % self.name


foo = Person()
# foo.__init__("w")
# bar = Person()
foo.setName('Howie')
my_name = foo.getName()
print(my_name)
foo.greet()

