l=[1,3,3,2,5,4,6,1]
nondup=[]
dup=[]
unique=[]

for i in range(len(l)):
    if l[i] not in nondup:
        nondup.append(l[i])
    elif l[i] in nondup and l[i] not in dup:
        dup.append(l[i])
for i in nondup:
    if l[i] not in dup:
        unique.append(l[i])

print(nondup)
print(dup)
print(unique)