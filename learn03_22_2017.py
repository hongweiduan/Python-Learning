class MyDecriptor(object):
    """docstring for MyDecriptor"""
    def __init__(self):
        super(MyDecriptor, self).__init__()
    def __get__(self,instance,owner):
        print("getting...",self,instance,owner)
    def __set__(self,instance,value):
        print("setting...",self,instance,value)
    def __delete__(self,instance):
        print("delete...",self,instance)
class Test(object):
            """docstring for Test"""
            def __init__(self):
                super(Test, self).__init__()
            x = MyDecriptor()  

class Celsius:
    def __init__(self,value = 26.0):
        self.value = float(value)
    def __get__(self,instance,owner):
        print("getting.....")
        return self.value
    def __set__(self,instance,value):
        self.value = float(value)
    def __delete__(self,instance):
        del self.instance
class Fahrenheit:
    def __get__(self,instance,owner):
        return instance.cel*1.8+32
    def __set__(self,instance,value):
        instance.cel = (float(value)-32)/1.8
class Temperature:
    cel = Celsius()
    fah = Fahrenheit()

temp = Temperature()
print(temp.cel) #in Python3 will return the attribute@@@@but in Python2 will just return a instance?
temp.fah = 13   # I think in Python2 have None __get__() function
print(temp.cel)

class Countlist(object):
    """docstring for Countlist"""
    def __init__(self, *arg):
        super(Countlist, self).__init__()
        self.values = [x for x in arg]
        self.count = {}.fromkeys(range(len(self.values)),0)
    def __len__(self):
        return len(self.values)
    def __getitem__(self,key):
        self.count[key] +=1
        return self.values[key]
c1 = Countlist(1,2,3,4,5)
c2 = Countlist(2,3,4,5,6)
c1[2]
c2[1]
c1[3]+c2[1]
# print (c1.count)
dict_1 = {"1":"www.baidu.com",\
"2":"www.sina.com.cn"
}
for x in "xrange(1,10)":
    print(x)
for each in dict_1:
    print("%s -> %s"%(each,dict_1[each]))
string = "Howie"
it = iter(string)
next(it)
print(next(it))  
it1 = iter(string)
while 1:
    try:
        each = next(it1)
    except StopIteration:
        break
    print(each)
class Fibs:
    """docstring for fibs"""
    def __init__(self,n = 20):
        self.n = n
        self.a = 0
        self.b = 1
    def __iter__(self):
        return self
    def __next__(self): # in Python2 it don't have this magic methods
        self.a,self.b = self.b,self.a+self.b
        if self.a>self.n:
            raise StopIteration
        return self.a
fibs = Fibs(500)
for x in fibs:
    print(x)
    # if x<50:
    #     print(x)
    # else:
    #     break         
