#coding:utf-8

#####6.4 parameter in function#######
# def change_param(param):
# 	param = param +1
# 	return param
# a = 10
# change_param(a)
# print a
# a = change_param(a) # this way will be well
# print a
# def change_param_use_list(param):
# 	param[0] = param [0] +1
# b = [10]
# change_param_use_list (b)
# print b


# def keyword_param(name,age):
# 	print "%s is %d years old!" % (name ,age)
# keyword_param("Howie",23)
# keyword_param(name = "Howei",age = 23)
# #keyword_param(name = "DD",height = 175)  # a bad keyword will not be accepted
# #keyword_param(name = "DD",height = 175 , age = 23 )
# def keyword_param(name = "Everybody" ,age = 18):  # keyword parameter will set a default param
# 	print "%s is %d years old!" % (name ,age)
# keyword_param()
# keyword_param("Howie",age = 23)
# #def two_kinds_of_param(name = "Everybody",age = 18, height):  # location parameter must be in front of keyword paramter
# def two_kinds_of_param(name,age = 18, height =175):
# 	print "%s is %d years old!And is %d cm tall" % (name ,age ,height)
# two_kinds_of_param("Howie",23,175)


#collect_param

# def init(data):
# 	data['first']={}
# 	data['middle']={}
# 	data['last']={}
# storage ={}
# init(storage)
# def lookup(data,label,name):
# 	return data[label].get(name)

# def store(data,*full_name):
# 	for full_name in full_name:
# 		name = full_name.split()
# 		if len(name)==2:
# 			name.insert(1,"")
# 		label = 'first',"middle","last"
# 		for label,name in zip(label,name):
# 			people = lookup(data,label,name)
# 			#print people
# 			if people:
# 				people.append(full_name)
# 				#print data
# 			else:
# 				data[label][name]=[full_name]
# 				#print data
# #lookup(storage,'middle','Lie')
# store(storage,"Magnus Lie HH","Howie Duan")
# store(storage,"FFJS Lie HH")
# print storage


def story(**kwds):
	return 'Once upon a time, there was a ' \
			'%(job)s called %(name)s.' % kwds

def power(x,y,*others):
	if others:
		print 'Received redundant parameters:',others
	return pow(x,y)

def interval(start,stop = None,step=1):
	'Imitates range() for step > 0'
	if stop is None:
		start,stop = 0 , start
	result = []
	i = start
	while i < stop:
		result.append(i)
		i += step
	return result
#####################
print story(job = 'King',name = 'Howie')
print

