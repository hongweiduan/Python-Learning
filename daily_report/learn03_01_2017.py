##Timer##
import time
from string import Template
# print(help(time))
# print(time.time())

class Timer(object):
	"""This class is for Timer,You can add two Timer """
	def __init__(self, lable="My Timer"):
		super(Timer, self).__init__()
		self.lable = lable
		self.__start_time = -1
		self.__end_time = -1
	def __str__(self):
		if self.__start_time == -1:
			return "You need Start"
		if self.__end_time == -1:
			self.__end_time =time.time()
			self.run_time =self.__end_time - self.__start_time
			return 'Run %d S' % self.run_time
		if self.run_time == 0:
			return 'You need run a Timer first!'
		else:
			return 'Run %d S' % self.run_time
	def __add__(self,other):
		return 'Run %.4f S' % (self.run_time + other.run_time)
	def start(self):
		self.__start_time = time.time()
		print('Starting!')
	def stop(self):
		if self.__start_time == -1:
			print("You need Start")
		else:
			self.__end_time = time.time()
			print('Stoping!')
			self.run_time =self.__end_time - self.__start_time
# t1 = Timer()
# t1.stop()
# print(t1)
# t1.start()
# time.sleep(3)
# t1.stop()
# print(t1)
# t2 = Timer()
# t2.start()
# time.sleep(2)
# t2.stop()
# # print(t2)
# print(t1+t2)

class C(object):
	"""docstring for C"""
	def __init__(self,arg=None):
		super(C, self).__init__()
		self.arg = arg
	def __getattribute__(self,name):
		print('getattribute')
		return super(C,self).__getattribute__(name)
c = C()
# c.arg

class A(object):
  def __init__(self):
   print "enter A"
   print "leave A"
  def class_name(self):
  	print 'class------A'

class B(object):
  def __init__(self):
   print "enter B"
   print "leave B"

class C(A):
  def __init__(self):
   print "enter C"
   super(C, self).__init__()
   super(C, self).class_name()
   super(C, self).do_nothing()
   print "leave C"

class D(A):
  def __init__(self):
   print "enter D"
   super(D, self).__init__()
   print "leave D"
  def class_name(self):
  	print 'class------D'
  def do_nothing(self):
  	pass
class E(B, C):
  def __init__(self):
   print "enter E"
   super(E,self).__init__()
   print "leave E"

class F(E, D):
  def __init__(self):
   print "enter F"
   super(F,self).__init__()
   print "leave F"
# print "MRO:", [x.__name__ for x in F.__mro__]
# f = F()
class Rectangle(object):
	"""docstring for Rectangle"""
	def __init__(self, length = -1, wide = -1, square = -1):
		super(Rectangle, self).__init__()
		self.length = length
		self.wide = wide
		self.square =square
	def get_area(self):
		if self.square ==-1:
			return self.length*self.wide
		else:
			return self.square*self.square

a = Rectangle(square = 3)
# print(a.get_area())
class my_decriptor(object):
	"""docstring for my_decriptor"""
	def __init__(self):
		super(my_decriptor, self).__init__()
	def __get__(self,instance,owner):
		print("gggg",self,instance,owner)
class Test(object):
	"""docstring for Test"""
	def __init__(self):
		super(Test, self).__init__()
	x =my_decriptor()
# test = Test()
# test.x

#c*1.8+32

class my_property(object):
			"""docstring for my_propoty"""
			def __init__(self, fget,fset,fdel):
				super(my_property, self).__init__()
				self.fget = fget
				self.fset = fset
				self.fdel = fdel
			def __get__(self,instance,owner):
				return self.fget(instance)
			def __set__(self,instance,value):
				self.fset(instance,value)
			def __delete__(self,instance):
				self.fdel(instance)
class C(object):
	"""docstring for C"""
	def __init__(self):
		super(C, self).__init__()
		self._x = None
	def get_x(self):
		return self._x
	def set_x(self,value):
		self._x = value
	def del_x(self):
		del self._x
	x = my_property(get_x,set_x,del_x)
c = C()
print c._x
c.x =1
print c._x
print (c.x)
del c.x

class Temperature(object):
	"""docstring for Temp"""
	def __init__(self):
		super(Temperature, self).__init__()
		self._temp_C = None
	def get_c_temp(self):
		return self._temp_C
	def set_c_temp(self,value):
		self._temp_C = value
	def del_c_temp(self):
		del self._temp_C
	c_temp = my_property(get_c_temp,set_c_temp,del_c_temp)
	def get_f_temp(self):
		return (self._temp_C*1.8+32)
	def set_f_temp(self,value):
		__long_float_temp = (int(value)-32)/1.8
		self._temp_C = '%.1f' % __long_float_temp
	def del_f_temp(self):
		del self._temp_C
	f_temp = my_property(get_f_temp,set_f_temp,del_f_temp)
temp = Temperature()
temp.c_temp = 32
print temp.f_temp
temp.f_temp = 42
print temp.c_temp

a = vars(Timer)
print(a)
'''
----------------------------------------------------------------------------
'''
class DynamicObject:

    def __init__():
        """ This is an object that is provides useful functions when dynamically
        loading the object from a freeform dictionary - by matching keys to
        local variable names. """
        self.ignoredKeys = []
        self.notSetOnChildren = []
        self.defaultRecursiveNamedKey = None

    def parse_project_dictionary(self, loadedObject, warn_if_not_in_object=True, recursive_key=None, is_child=False, child_class=None, called_after_update=None):
        """ Loads new values into this object for the keys specified in loadedObject.
            If projects is specified - it will recursively initialize the new project"""

        if recursive_key is None:
            recursive_key = self.defaultRecursiveNamedKey

        selfVars = vars(self)

        for key, value in loadedObject.items():
            if key in self.ignoredKeys:
                continue
            elif is_child and key in self.notSetOnChildren:
                continue
            elif key in selfVars:
                if type(value) is dict and type(selfVars[key]) is not dict:
                    selfVars[key] = self.load_property_from_dictionary(value)
                elif value:
                    selfVars[key] = value
            elif warn_if_not_in_object:
                print "Key ({0}) not a valid key for the station build description - run --help_json_description to see valid keys".format(key)

        if called_after_update is not None:
            called_after_update()

        if recursive_key is None:
            recursive_key = self.defaultRecursiveNamedKey

        # Set new updated properties on all children
        for childName, child in selfVars[recursive_key].items():
            child.parse_project_dictionary(loadedObject, warn_if_not_in_object=False, is_child=True, recursive_key=recursive_key)

        # Create children if needed (overrides - does not merge existing children)
        if not is_child and recursive_key and recursive_key in loadedObject:  # Special - means that this is a container class
            for childName, childInfo in loadedObject[recursive_key].items():
                if child_class is None:
                    child = self.__class__(childName)
                else:
                    child = child_class(childName)
                child.parse_project_dictionary(selfVars, warn_if_not_in_object=False, is_child=True)
                child.parse_project_dictionary(childInfo, warn_if_not_in_object=warn_if_not_in_object, recursive_key=recursive_key, called_after_update=called_after_update)
                selfVars[recursive_key][childName] = child

    def load_property_from_dictionary(self, value):
        if "environmentVariable" in value:
            if value["environmentVariable"] in os.environ:
                return os.environ[value["environmentVariable"]]

        if "default" in value:
            return value["default"]

        Logger.warn("Dictionary for non-dictionary property does not contain 'default' or 'environmentVariable' fields")
        return value


    # Class convenience methods

    def set_property_recursively(self, property_name, to_value=None, recursive_key=None):
        if to_value is None:
            to_value = vars(self)[property_name]
        self.parse_project_dictionary({property_name: to_value}, recursive_key="projects")


    def safely_recurse_calling(self, method_name, recursive_key=None, arguments=[], kwargs={}):

        if recursive_key is None:
            recursive_key = self.defaultRecursiveNamedKey

        if recursive_key is None or recursive_key not in vars(self):
            return

        if arguments is None:
            arguments = []

        if kwargs is None:
            kwargs = []

        for project_name, project in vars(self)[recursive_key].items():
            method = getattr(project, method_name)
            if not method:
                Logger.error("Method %s not implemented" % method_name)
            elif len(kwargs) != 0 and len(arguments) != 0:
                method(*arguments, **kwargs)
            elif len(kwargs) != 0:
                method(**kwargs)
            elif len(arguments) != 0:
                method(*arguments)
            else:
                method()

    def replace_keys_in_string(self, string, overrideDictionary=None):

        oldString = None
        while string != oldString:
            oldString = string
            if overrideDictionary is not None:
                string = Template(string).safe_substitute(overrideDictionary)
            string = Template(string).safe_substitute(vars(self))
        return string

    # TODO: Doesn't need to be method of class
    def iterate_through_property_list(self, propertyList, function, *args):
        if type(propertyList) is list:
            for thisProperty in propertyList:
                function(thisProperty, *args)
        else:
            function(propertyList, *args)

atlas  = DynamicObject
# print (atlas.parse_project_dictionary(atlas))	

