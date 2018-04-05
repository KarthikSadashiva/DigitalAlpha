lower_limit = int(input("Enter the lower limit of the range for Armstrong number : "))
upper_limit = int(input("Enter the upper limit of the range for Armstrong number : "))
armstrong = []
for i in range(lower_limit,upper_limit+1):
    length = len(str(i))
    if(sum(int(j)**length for j in str(i)) == i):
        armstrong.append(i)
        print(i," is Armstrong number")
