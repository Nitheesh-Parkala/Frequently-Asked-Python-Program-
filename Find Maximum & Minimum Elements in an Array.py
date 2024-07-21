arr=[30,20,14,40,26,21]


#Finding Max 
max=arr[0]
for i in range(1,len(arr)):
    if(arr[i]>max):
        max=arr[i]
print(max)

#Finding Min
min=arr[0]
for i in range(1,len(arr)):
    if(arr[i]<min):
        min=arr[i]
print(min)

