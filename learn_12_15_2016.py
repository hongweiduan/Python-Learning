#coding:utf-8

#############6.5---global and local ------

# def x_and_one(x):
# 	x = x + 1
# 	return x
# def global_x_and_one():
# 	global x
# 	x = x + 1
# 	return x
# x = 2
# x_and_one(x)
# print(x)
# x = x_and_one(x)
# print(x)
# global_x_and_one()
# print(x)
def factorial(n):
	if n == 1:
		return 1
	else:
		return n*factorial(n-1)
print(factorial(3))

def power(x ,n):
	if n == 1:
		return x
	else:
		return x * power (x,n-1)
print(power(2,3))