sentence = input("Enter the sentence with digits and alphabets : ")
alphabets = 0
digits = 0
for i in sentence:
    if(i.isalpha()):
        alphabets = alphabets+1
    elif(i.isdigit()):
        digits = digits+1
print("There are ",alphabets,"letters and ",digits,"digits in the given sentence.")        