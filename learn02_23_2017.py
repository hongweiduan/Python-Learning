#coding:utf-8
# try:
# 	sum =1 +'w'
# 	f = open('ssss.txt')
# 	print(f.read())
# 	f.close()
# except FileNotFoundError as e:
# 	print(str(e))
# except TypeError as e:
# 	print(str(e))
# else:
# 	pass
# finally:
# 	pass


# try:
# 	sum =1 +'w'
# except Exception as e:
# 	print(str(e))
# else:
# 	pass
# finally:
# 	pass
# 	# f = open('ssss.txt')
# 	# print(f.read())
# 	# f.close()

box = [1]*100
for i in range(2,101):
	for n in range(1,100):
		j = i*n
		if j<=100:
			# print(j)
			if box[j-1] == 0:
				box[j-1] = 1
			else:
				box[j-1] = 0
		else:
			break
# print (box)
for i in range(0,99):
    if box[i]:
        print(i+1, end=' ')
# print
print(sum(box))

box = [-1] * 100
for i in range(1,101):
    for n in range(1, 101):
        if (i * n - 1) < 100:
            box[i * n - 1] = -box[i * n - 1]
        else:
            break
for i in range(100):
    if box[i] == 1:
        print('第',i+1,'个箱子是打开的')
c = box.count(1)
print('共有', c, '个箱子打开')
