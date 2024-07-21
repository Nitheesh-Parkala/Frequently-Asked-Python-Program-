# 5!=1*2*3*4*5

factorial=1
num =26
i=1
if(num<0):
    print("Factorial is not exits for a negative number")
elif(num==0):
    print("Factorial of 0 is 1")
else:
    # for i in range(1,num+1):
    while(i<=num):
        factorial = factorial * i
        i+=1
    print("The Factorial of",num,"is",factorial)

    #Using Recursion...
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
num =21
print("Factorial of ",num,"is",factorial(num))