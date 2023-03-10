#Olivia Busk

#Problem 4
total=0
def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        result=fibonacci(n-1)+fibonacci(n-2)
        return result

print(fibonacci(4))

# Problem 1 exit using control c
#while 1==True:
#    print("How are you today?")


#Problem 2
i=2
sum=0
while i <12:
    sum+=i
    i+=2
print("the sum of all postive numbers less than 12 is", sum)
