#Factorial of Given Number

num = int(input(" Please Enter the Number : "))
fact = 1
if(num == 0 or num == 1):
    print(f' Factorial of {num} = {fact}')
else:
    for i in range(1,num+1):
        fact = fact * i
    print(f' Factorial of {num} = {fact}')
