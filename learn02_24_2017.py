#coding:utf-8
# raise ZeroDivisionError("异常")
def showMaxFactor(num):
	count = num //2
	while count >1:
		if num % count == 0:
			print("%d 's max factor is %d" % (num,count))
			break
		count -= 1
	else:
		print('%d is a prime number' % num)
num = int(12)
showMaxFactor(num)

with open('learn.py','r') as f:
	for each_line in f:
		print(each_line)
