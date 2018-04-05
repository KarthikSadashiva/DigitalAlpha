print("With this calculator you can calculate the factorial of a number, LCM and HCF of a number and also factors of the number ")
user_choice = int(input("Press\n\t1.Factorial of the number\n\t2.LCM of the number\n\t3.HCF of the number\n\t4.Factors of the number\nEnter your choice : "))
def HCF(a,b):
    while(b>0):
        a,b = b,a%b
    return a  
def LCM(a,b):
    return a*b/HCF(a,b)
if(user_choice == 1):
    number = int(input("Enter the number for which you want to find the factorial : "))
    factorial = 1
    for i in range(1,number+1):
        factorial = factorial*i
    print(factorial)
elif(user_choice == 2):
    a = int(input("Enter the first number for LCM : "))
    b = int(input("Enter the second number for LCM : "))
    print("The LCM of ",a,b," is ",LCM(a,b))
elif(user_choice == 3):
    a = int(input("Enter the first number for HCF : "))
    b = int(input("Enter the second number for HCF : "))
    print("The HCF of ",a,b," is ",HCF(a,b))
elif(user_choice == 4):
    n = int(input("Enter the number for which you need to calculate factors : "))
    factors = []
    for i in range(2,n+1):
        if(n%i == 0):
            factors.append(i)
    print(factors)