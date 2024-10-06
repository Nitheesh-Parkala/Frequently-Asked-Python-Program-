def findMaxElement(l):
   max=-2147483648
   secmax=-2147483648
   for i in range(len(l)):
      if max<l[i]:
         secmax=max
         max=l[i]
      elif secmax<l[i] and max!=l[i]:
         secmax=l[i]  
   return max,secmax

l=[1,2,3,5,6,7,21,26]

res,res1=findMaxElement(l)
print(res)
print(res1)