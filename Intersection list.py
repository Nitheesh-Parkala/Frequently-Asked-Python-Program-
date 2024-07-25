#1 approach
a=[10,20,30,40]
b=[20,30,7,1]
c=[]

for i in a:
    if i in b: 
        c.append(i)
print(c)

#2 approach
a=[1,20,30,40]
b=[20,30,7,1]
c=[]

for i in a:
    for j in b:
       if(i==j): 
        c.append(i)
print(c)