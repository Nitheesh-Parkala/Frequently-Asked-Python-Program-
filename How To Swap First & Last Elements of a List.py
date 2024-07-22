# Approach1: Temporary Variable

myList=[21,7,17,18,26]
print("List Before swapping:", myList)

size= len(myList)

temp= myList[0]
myList[0]=myList[size-1]
myList[size-1]=temp

print("List After swapping:", myList)

# Approach2: index 

myList=[21,7,17,18,26]
myList[0],myList[-1]=myList[-1],myList[0]
print(myList)