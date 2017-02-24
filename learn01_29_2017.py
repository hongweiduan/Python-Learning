#!/usr/bin/env python 
# -*- coding: utf-8 -*- 

# class Filter:
# 	def init(self):
# 		self.blocked = []
# 	def filter(self,sequence):
# 		return [x for x in sequence if x not in self.blocked]
# class SPAMFilter(Filter):
# 	def init(self):
# 		self.blocked = ['SPAM']
# f = Filter()
# f.init()
# print f.filter([1,2,3])
# s = SPAMFilter()
# s.init()
# print s.filter(["SPAM","SSSS","SPAM","SPAMA"])
# class newFilter(Filter):
# 	def setBlocked(self,newBlocked):
# 		self.blocked = newBlocked
# n = newFilter()
# n.init()
# n.setBlocked(["SPAM","SSSS"])
# print n.filter(["SPAM","SSSS","SPAM","SPAMA"])
 
# print issubclass(Filter,SPAMFilter)
# print issubclass(SPAMFilter,Filter)
# print newFilter.__bases__
# print Filter.__bases__
# print s.__class__

class Calculator:
	def calculator(self,expression):
		self.value = eval(expression)

class Talker:
	def talk(self):
		print "Hi, my value is ",self.value

class TalkingCalculator(Calculator,Talker):
	pass	

n = TalkingCalculator()
n.calculator("3+5")
n.talk()
		
print hasattr(n,'talk')	
print hasattr(n,'ss')	
print callable(getattr(n,'ss','have ss'))
setattr(n,'name','Howie')
print n.name
print hex(58)		
print type(TalkingCalculator)

		