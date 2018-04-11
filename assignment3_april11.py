import math
n = int(input("Enter the value of n : "))
print("Sum of numbers is",sum(range(1,n+1)))
divisible_by_n = []
for i in range(501):
    if(i%n == 0):
        divisible_by_n.append(i)
print("The numbers divisible by",n,"are",divisible_by_n)
final_sum=0
for i in range(0,3):
    sum1=0
    while i>=0:
        sum1=sum1+(math.pow(10,i)*n)
        print(sum1)
        i=i-1
    final_sum=final_sum+sum1    
print(final_sum)
inv = []
for i in range(1,n+1):
    inv.append(1./i)
print(sum(inv))
