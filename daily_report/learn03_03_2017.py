import urllib.request
import re
import os
path = os.getcwd()

request = urllib.request.urlopen('http://www.zdt8.com/new/')
req = request.read().decode('utf-8')
q = re.compile ('http://pic1.zdt8.com/p/\d*?-\d*?-\d*?/\w*?.jpg')

f_name = re.compile ('alt=".*?"')
f_name_list =f_name.findall(req)
f_name_list.remove (f_name_list[0])
m = q.findall(req)
big_pic_url = re.compile ('http://www.zdt8.com/meitu/\w*?.html')
all_url = big_pic_url.findall (req)
def fun (urllist,num):
    
    
    w = []
    for url2 in urllist:
        w.append(url2[8:])
        print (w[0][23:33])
        
    print ('the%d‘s o(*￣▽￣*)o'%(num))
    
        
    return w
    
def get_bigpic(url_list):
    q= []
    a= 1
    for url in url_list:
        
        
        
        request = urllib.request.urlopen(url)
        req1 = request.read().decode('utf-8')
        big_p_url = re.compile ('lazysrc=http://pic1.zdt8.com/p/\d*?-\d*?-\d*?/\w*?.jpg')
        
        url = big_p_url.findall(req1)
        
        
        q.extend(fun(url,a))
        a+=1
    
    
        
    
    return q
    
q1 = get_bigpic(all_url)

os.makedirs (path+'/'+m[0][28:33])
print(path+'/'+m[0][28:33])
os.chdir (path+'/'+m[0][28:33])


def a (url_list,name):
    a=0
    print('*********************Save in local******************************')
    for url in url_list:
        




        response = urllib.request.Request (url)
        rs = urllib.request .urlopen (response)
        print(name[a][5:-1]+'.jpg')
        f = open(name[a][5:-1]+'.jpg','wb')
        f.write(rs.read())
        f.close()
        a= a+1
    print('Save Successful')
       
a(q1,f_name_list)