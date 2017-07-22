#coding:utf-8

#list

member = ["as",1,["sss",2]]
print member
member.append("lalala")
print member
member.extend(["ss",2])
print member
member.extend(member)
print member
member = member * 4
print member
member.insert(len(member),"mudan")
print member
member.remove("lalala")
print member
del member[1]
print member
pop_str = member.pop()
print pop_str