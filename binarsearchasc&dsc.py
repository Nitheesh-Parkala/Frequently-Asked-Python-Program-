l1=[8,7,6,5,4,3,2]
flag="asc"
if (l1[0]>l1[len(l1)-1]):
    flag="dsc"

start=0
end=len(l1)-1
flag=-1

target=3

while(start<=end):
    mid=(start+end)//2

    if target==l1[mid]:
        flag=mid
        break

    if flag=="asc":
        if(target<mid[l1]):
            end=mid-1
        else:
            start=mid+1
    else:
        if(target<l1[mid]):
            start=mid+1
        else:
            end=mid-1
print(flag)

        

    