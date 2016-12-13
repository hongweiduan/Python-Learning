#coding:utf-8
#############6 -----function ------
########6.4 -----parameter-----
def init(data):
	data['first']={}
	data['middle']={}
	data['last']={}
storage ={}
init(storage)
def lookup(data,label,name):
	return data[label].get(name)

def store(data,full_name):
	name = full_name.split()
	if len(name)==2:
		name.insert(1,"")
	label = 'first',"middle","last"
	for label,name in zip(label,name):
		people = lookup(data,label,name)
		#print people
		if people:
			people.append(full_name)
			#print data
		else:
			data[label][name]=[full_name]
			#print data
#lookup(storage,'middle','Lie')
store(storage,"Magnus Lie HH")
store(storage,"FFJS Lie HH")
#print storage
#print lookup(storage,'middle','Lie')


#############5---- if&for&while -------
##########5.1--print import---
# print ((1,2+3,4))
# print 1,2
# print 1,(2,3)
# print (1,2,3)
# print 'jjj','ss'
# from math import pi as p # from import as that's cool
# from math import pi
# print p
# print pi
#########5.2 ---assignment------
# values = 1,2,3,4
# x,y,_,_ = values # sequence unpacking
# print x
# x=y=values #chained assignment
# x+=(1,)
# x*=5
# print x
#########5.4-------if ------
# print bool("")==bool([])
# print "" == []
# name  = ""
# if name.endswith("Howie"):
# 	if name.startwith("Mr."):
# 		print "Hello Mr.Howie"
# 	elif name.startwith("Mrs."):
# 		print "Hello Mrs.Howie"
# 	else :
# 		print "Hello Howie"
# else:
# 	print "Hello Stranger"
# print ([1,2]>[2,1])
# print (not True is (not ""))
# a =-1
# if 0<=a<=10:
# 	print "pass"
# b = "a"
# a = b or 1000     ### so cooooooool!!!
# print a 
# assert a != 1000 , "input is nil"  # assert is helpful
# name = "nn"
# while not name or name.isspace():  # s.isspace() if s is a space then return Ture else return False
# #while not name.strip(): #s.strip(rm) remove rm in the s' head and end  if rm is nil than remove the "\r\n\t" 
# 	##strip[dict:remove something that is covering the surface of somthing else]
#  	name = raw_input("Please enter your name")
# print "Hi "+name
# print "Hi %s" % name 
# a = "123211aaa22222"
# a = a.strip("12") # input is "3211aa"
# print a
# name = range(1,101) # range()
# name = ["A","B","C","D"]
# for i in name:
# 	print "Hi %s" % i
# for_dict = {"x":1,"y":2 ,"z": 3}
# for key in for_dict:
# 	print key+" corresponds to " + str(for_dict[key])
# name = ["A","B","C","D"]
# age = [1,2,3,4]
# name_age = zip(name,age)
# name_age_dict = dict(name_age)
# print name_age_dict
# for key in name_age_dict:
# 	print key
# for name,age in name_age:
# 	print name + " is " + str(age) + " years old"

# a = ["ssxxx","sawa",'saoxxx']
# i = 0 



# for str_current in a:
# 	if "xxx" in str_current:
# 		index = a.index(str_current)
# 		a[index] = "got it"
# for j in a:
# 	if "xxx" in j:
# 		a[i] = "got it"
# 	i+=1
# for index,vaule in enumerate(a):
# 	if "xxx" in vaule:
# 		a[index] = "got it"
# print a
# from math import sqrt as pingfanggen
# for x in xrange(99,0,-1):
# 	s = pingfanggen(x)
# 	if s == int(s):
# 		print x
# 		break
# else:
# 	print "No one"
# girls  = ["aaa","bbb","ccc"]
# boys = ["ab","bb","ca"]
# lettergirls ={}
# for girl in girls:
# 	lettergirls.setdefault(girl[0],[]).append(girl)
# # print lettergirls
# #{'a': ['aaa'], 'c': ['ccc'], 'b': ['bbb']}
# #{'a': 'aaa', 'c': 'ccc', 'b': 'bbb'}
# 	lettergirls[girl[0]] = girl
# 	#lettergirls[girl[0]] = [girl]
# print lettergirls
# print lettergirls["b"]
# #print [g + "---" +b for b in boys for g in lettergirls[b[0]] ]	
# print [lettergirls[b[0]] + "---" +b for b in boys ]
# for x in xrange(1,10):
# 	# if x ==2:
# 	# 	break
# 	if x == 3:
# 		continue
# 	print x
# 	if (not x==4):
# 		print x
#



#
#
#   3 lines love letter
#
# if (not bool("Mountain with edges"))&("River" is "exhaust"):
# 	print("I leave you.")
# else : print'\n'.join([''.join([('ILoveYou'[(I-You)%7]if((I*0.05)**2+(You*0.1)**2-1)**3-(I*0.05)**2*(You*0.1)**3<=0 else' ')for I in range(-30,30)])for You in range(15,-15,-1)])

#############4----Dictionary----#########
# def Get4WOhmData():
# 	pass
# list_a = dict(name="CC1 Plug A5 to CC1 wire-pad",lower=0,upper=60,unit="mohm",entry=Get4WOhmData,parameter="SBIT001,019,018,017,015,022,021,020=1,0,1,0,1,0,0,1",visible=1)
# print list_a
# list_a = ['s','c','hg']
# #list_a[9]='sss' #It's wrong
# list_a[len(list_a)-1]='sss'
# print list_a
# dict_a ={1:'ds',2:'ssss'}
# dict_a[5] = 'sds' #That's OK
# print dict_a
# a=0000000000040000
# print "%d" %a
##-------------4.2.4 dictionary function-----
#---clear---
# d = {}
# d['1'] = 13
# y = d
# print y
# d = {} # can clear d but can't clear y 
# print y
# d.clear() # can clear d and y
# print y
#---copy---
# from copy import deepcopy
# a  = {"first":"1st","second":["2nd",2]}
# #b = a.copy()
# b = deepcopy(a) ##need to take notice of it //b = deepcopy(a) Yes b = a.deepcopy() NO
# a["second"].remove("2nd")
# print b
# print a
#---fromkeys--- 
# b_list = ["zhangsan","lisi","wangwu"]
# a = dict.fromkeys(b_list,"No money") # param1 is a list for dict key, param2 is a default value
# # print a
# #---get---
# #print a["lisi2"] #if key is not in dict ,will return keyError : "the error key you called "
# #print a.get('lisis') # if key is not in dict , will return None instead of a error
# #print a.get ('wangchao','Nomoney') # and will return default value 
# #print a # but don't change the dict
# #---items & iteritems & keys & iterkeys
# print a.items()
# print a
# for i in a.iteritems():
# 	print i[0]
# 	print a[i[0]]
# print a.keys()
# for i in a.iterkeys():
# 	print i
# 	print a[i]
# #---popitem()
# n = a.keys()
# print len(n)
# for i in xrange(0,len(n)):
# 	print a.popitem()
# print a
# #---setdefault---
# a.setdefault('zzzz','100')
# print a
# a['s'] = '2' # I don't know the different between two code -|-
# print a
# a['s'] = '200'
# print a
# b = {'s':'23','add':'oo'}
# #---update---
# a.update(b)
# print a
# #---values & itervalues---
# print a.values()
# for i in a.itervalues():
# 	print i
# 	print i in a.values()
#---
# ---------A DataBase -------------
# people = {
# 	'Alice':{
# 		'phone':'2341',
# 		'addr':'Foo drive 23'
# 	},
# 	'Beth':{
# 		'phone':'9102',
# 		'addr':'Bad drive 12'
# 	},
# 	'Cecil':{
# 		'phone':'1124',
# 		'addr':'Gold drive 12'
# 	}
# }
# labels = {
# 	'p':'phone',
# 	'a':'addr'
# }

# name = 'Alice'
# if name in people :
# 	print 's'
	#print name + '\'s Phonenumber is ' + people[name][labels['p']] + ',addr is ' + people[name][labels['a']]
	#print '%ss phone number is %(phone)s.' % (name,people[name])
#############3----String---##############
#############3.1--format############
# from math import pi
# format = "Hi,%s! good %s! in %d %d%% %*.3E,%.2G %c" 
# tuple = ("Howie","Job",070,10,20,pi,132,"a")
# print format % tuple
# from string import Template
# who_do_something = Template("$who $action $something")
# cat = {'who':'Cat','action':'eat','something':'fish'}
# dog = {'who':'Dog','action':'eat','something':'meat'}
# Ultrman = {'who':'Ultrman','action':'beat','something':'small monster'}
# print who_do_something.substitute(cat)
# print who_do_something.substitute(dog)
# print who_do_something.substitute(Ultrman)
#----------------for a price list --------- TBD
# item_width = 10
# price_width = 8
# header_width = item_width + price_width +5
# input_list = {'Apple':0.4,
# 'Pears':0.5,
# 'Cantaloupes':1.92,
# 'Dried Apricots (16 oz.)':8,
# 'Prunes (4 lbs)':12,
# }
# print input_list
#------------------------------------------
#from string import capwords
# title = 'last find ss ok python'
# a = title.find('ss ok')
# print a
# d_list = ['Desktop','test.py']
# c = '/'.join(d_list) #sep.join(seq)
# c = c.title() # lower upper title
# print c
# my_str = '&#$I like apple apple****'
# print my_str.replace('apple','banana') #string.replace(need_find,to_change)
# #if don't find it ,It will do nothing
# my_str = my_str.strip(' *&$(#')
# my_list = my_str.split(' ')
# print my_list
# from string import maketrans
# table = maketrans('csia','kzai')
# my_str = my_str.translate(table)
# print my_str
#############2.4--TUPLE#########################
# a = 1,
# print a
# b = ['a','b','c']
# c = tuple(b) # don't change the list
# d = c[0:2]
# print b
# print c
# print d
##############2.3--LIST -- list function ###############
# a= [1,2,3]
# b= [2,3,4]
# a.extend(b) # extend the list by a list 
# print a
# a= a+b
# print a
# c = a.index(4) #return the first index of value
# print c
# a.insert(2,"as")
# print a
# a.pop(2) # remove by the key
# print a
# a.append(a.pop()) # LIFO
# print a
# a.insert(0,a.pop(0)) # FIFO
# print a
# a.remove(2) #remove by the value
# print a
# a.reverse() #get a reverse list
# #-------- a test for iterator-------
# b = reversed(a) # get a reverse iterator & just can be used once 
# for i in b:
# 	print "$"
# 	print i

# for j in b: # can't use 'b', because it have been used once
# 	print "*"
# 	print j
# #----------------------
# print a
# a.sort() 
# print a
# l = ["aa","da","cc"]
# l.sort()
# print l
#x = ["adaa","sd","dsaaaaa","saa","s"]
# #print len(x[2])
# def getlen(a):
# 	return len(a)
# x.sort(key = getlen) # parameter of key will sort() by key
# print x
# def getindex(a):
# 	x = ["adaa","sd","dsaaaaa","saa","s"]
# 	return x.index(a)
# x.sort(key = getindex)
# print x

################ for Test ################

# parting_line = "--"*40

# number = [1,2,3,4,5,6,7,8,9,10]
# print number[0:10:2]
# print number
# print number[::-1]
# str_list = ["t"]
# print number + str_list

# print parting_line
# def in_to_box(par):
#     the_result_string = par
#     screen_width = 80
#     text_width = len (the_result_string)
#     box_width = text_width +6
#     left_margin = (screen_width - box_width) //2

#     print '\r\n'
#     print ' ' * left_margin + '+' + '-' *(box_width - 2 ) + '+'
#     print ' ' * left_margin + '|' + ' ' * text_width + '|'
#     print ' ' * left_margin + '|' + the_result_string + '|'
#     print ' ' * left_margin + '|' + ' ' * text_width + '|'
#     print ' ' * left_margin + '+' + '-' *(box_width - 2 ) + '+'
#     print '\r\n'

# in_to_box("hahahahhassssss")
# # coding=utf-8
# import sys, os
 
# list1Display = ['1', '2', '3']
# list2Display = ['abc', 'def', 'rfs']
# while list2Display != []:
#     # Prints the values to a stream, or to sys.stdout by default.
#     # Optional keyword arguments:
#     # file: a file-like object (stream); defaults to the current sys.stdout.
#     # sep:  string inserted between values, default a space.
#     # end:  string appended after the last value, default a newline.
#     # print 可以将值输出到指定的输出流(可以是文件句柄),若不指定，
#     # 则输出到stdout(标准输出)
#     # 一般我们使用的时候不加输出定向符“>>”到输出的file对象，本代码中对象是stdout
#     # 下面的print在stdout对象中每次输出两个值
#     print >> sys.stdout, list2Display.pop(), list1Display.pop()
# os.system( "pause" )

# #!/usr/bin/python
# #coding:UTF-8
# print "你你"


# #!/usr/bin/env Python #coding:utf-8
# import tornado.httpserver 
# import tornado.ioloop 
# import tornado.options 
# import tornado.web
# from tornado.options import define, options
# define("port", default=8009, help="run on the given port", type=int)
# class IndexHandler(tornado.web.RequestHandler): 
# 	def get(self):
# 		z = ''
# 		for i in xrange(1,10):
# 			y = ''
# 			for j in xrange(1,i+1):
# 				x = '%2d'%(j*i)
# 				#print x
# 				x = str(j) + '*' + str(i) + '=' + str(x) + '  '
# 				y = y + x
# 			z = z + y + '\r\n'
# 		#greeting = self.get_argument('greeting', 'Hello')
# 		#greeting = self.get_argument('greeting',gettable()) 
# 		self.write(z)
# 		self.write('aaa')
# if __name__ == "__main__": 
# 	tornado.options.parse_command_line()
# 	app = tornado.web.Application(handlers=[(r"/", IndexHandler)]) 
# 	http_server = tornado.httpserver.HTTPServer(app) 
# 	http_server.listen(options.port) 
# 	tornado.ioloop.IOLoop.instance().start()


# def gettable():
# z = ''
# for i in xrange(1,10):
# 	y = ''
# 	for j in xrange(1,i+1):
# 		x = '%2d'%(j*i)
# 		#print x
# 		x = str(j) + '*' + str(i) + '=' + str(x) + '  '
# 		y = y + x
# 	z = z + y + '\r\n'

# print z
# 	return z

# x = gettable()
# print x
# # a=[1,2,3,4,5,6,]
# # #print a
# # #b=a
# # b=[0]*len(a)
# # b[len(a)-1]=a[0]
# # for i in xrange(1,len(a)):
# # 	b[i-1]=a[i]
# # print b
# import random
# # print random.uniform(10,20)
# a = []
# number =40
# sum = 0
# for i in xrange(1,number):
# 	r = random.randint(0,100)
# 	a.append(r)
# 	sum = sum + r
# print a
# print sum
# average = sum / number
# print average
# b = []
# for i in xrange(1,number):
# 	if a[i-1] < average:
# 		b.append(a[i-1])
# print b
# def getmax(table):
# 	maxnumber = table[0]
# 	for i in xrange(0,len(table)):
# 		if table[i]>maxnumber:
# 			maxnumber = table[i]
# 		else:
# 			maxnumber = maxnumber
# 	table.remove(maxnumber)
# 	return maxnumber
# #print getmax(b) 
# #print b
# def  reverse(table):
# 	ret = []
# 	for i in xrange(0,len(table)-1):
# 		#ret[i] = table [len(table)-i]
# 		#print len(table)
# 		ret.append(table[len(table)-i-1])
# 	return ret

# def sorted1(table,r):
# 	ret=[]
# 	for i in xrange(0,len(table)):
# 		m = getmax(table)
# 		#print m
# 		ret.append(m)
# 	if r:
# 		return ret
# 	else:
# 		return reverse(ret)
# #d = [1,2,3,4]
# #print sorted1(b,False)
# #print sorted1(b,True)
# c = sorted1(b,True)
# print c


#!/usr/bin/env Python 
# coding=utf-8
# a, b = 0, 1
# for i in xrange(1,100):
# 	a, b = b, a+b
# print a

# from __future__ import division
# #from Node import Node
# #树节点
# class Node:

#     def __init__(self, val):
#         self.val = val
#         self.left = None
#         self.right = None

# def calculate(nums):
#     nums_possible = list_result(nums)
#     operators_possible = list_result(['+','-','*','÷'])
#     goods_noods = []
#     for nums in nums_possible:
#         for op in operators_possible:
#             node = one_expression_tree(op, nums)
#             if cal_tree(node) == 24:
#                 goods_noods.append(node)
#             node = two_expression_tree(op, nums)
#             if cal_tree(node) == 24:
#                 goods_noods.append(node)
#     map(lambda node: print_expression_tree(node), goods_noods)




# def cal_tree(node):
#     if node.left is None:
#         return node.val
#     return cal(cal_tree(node.left), cal_tree(node.right), node.val)


# #根据两个数和一个符号，计算值
# def cal(a, b, operator):
#     return operator == '+' and float(a) + float(b) or operator == '-' and float(a) - float(b) or operator == '*' and  float(a) * float(b) or operator == '÷' and float(a)/float(b)

# def one_expression_tree(operators, operands):
#     root_node = Node(operators[0])
#     operator1 = Node(operators[1])
#     operator2 = Node(operators[2])
#     operand0 = Node(operands[0])
#     operand1 = Node(operands[1])
#     operand2 = Node(operands[2])
#     operand3 = Node(operands[3])
#     root_node.left = operator1
#     root_node.right =operand0
#     operator1.left = operator2
#     operator1.right = operand1
#     operator2.left = operand2
#     operator2.right = operand3
#     return root_node

# def two_expression_tree(operators, operands):
#     root_node = Node(operators[0])
#     operator1 = Node(operators[1])
#     operator2 = Node(operators[2])
#     operand0 = Node(operands[0])
#     operand1 = Node(operands[1])
#     operand2 = Node(operands[2])
#     operand3 = Node(operands[3])
#     root_node.left = operator1
#     root_node.right =operator2
#     operator1.left = operand0
#     operator1.right = operand1
#     operator2.left = operand2
#     operator2.right = operand3
#     return root_node

# #返回一个列表的全排列的列表集合
# def list_result(l):
#     if len(l) == 1:
#         return [l]
#     all_result = []
#     for index,item in enumerate(l):
#         r = list_result(l[0:index] + l[index+1:])
#         map(lambda x : x.append(item),r)
#         all_result.extend(r)
#     return all_result

# def print_expression_tree(root):
#     print_node(root)
#     print ' = 24'

# def print_node(node):
#     if node is None :
#         return
#     if node.left is None and node.right is None:
#         print node.val,
#     else:
#         print '(',
#         print_node(node.left)
#         print node.val,
#         print_node(node.right)
#         print ')',

# if __name__ == '__main__':
#     calculate([1,2,3,4])