#Natural Number >1
#Which has only 2 factor 1 and itself
#19 => 1 and 19 =>Prime number
#24 => 1,2,6,etc => Not a Prime Number

num=3
count=0
i=1
if(num>1):
    # for i in range(1,num +1):
    while(i<=num):
        if((num%i)==0):
            count=count+1
        i+=1
            
    if(count==2):
        print("Number is prime")
    else:
        print("Number is Not a Prime")
