#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
# class Class:
# 	"""docstring for Class"""
# 	# def __init__(self, arg):
# 	# 	super(Class, self).__init__()
# 	# 	self.arg = arg
# 	__self_name = "self"
# 	def print_self(self):
# 		print self.__self_name
# 	def method(self,name):
# 		print "I have a self!"
# 		self.name = name

# def function():
# 	print "I don't have a self !"

# instance = Class()
# instance.method("www")
# instance.method = function
# instance.method()
# instance.print_self()
# print_my_self = instance.print_self
# print_my_self()
# # print instance.__self_name
# instance.__self_name = "my self"
# print instance.__self_name
# instance.print_self()
# instance._Secretive__self_name = "my new self"
# instance.print_self()	
## 可以通过__来将类中的变量转化为私有变量

# ###################################
# class C:
# 	print "It's a class C !"

# a = C()
# b = C()
## print 语句会在创建class C的命名空间时执行，当命名空间已经创建后，再次新建实例并不会重复执行该条指令。

####################################
class can_get_instance_num:
	instance_num = 0
	def init(self):
		can_get_instance_num.instance_num +=1
	def print_num(self):
		print self.instance_num
a = can_get_instance_num()
a.init()
a.print_num()
b = can_get_instance_num()
b.init()
b.print_num()