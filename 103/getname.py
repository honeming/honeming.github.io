import random
f=open('names.txt','r')
a=f.read().splitlines()
f.close()
n=a.pop(random.randint(0,len(a)-1))
f=open('names.txt','w')
f.write("\n".join(a))
f.close()
input("name:"+n+'\nleft:'+str(len(a)))