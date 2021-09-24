#Program To Print Sum of Square of First 'N' Natural Number

num = int(input(" Please Enter The Value of Number Till Where SUM Is Required : "))
SUM = 0
for i in range(1,num+1):
    SUM = SUM + (i * i)
print(f' The Sum of Square of First {num} = {SUM} ' )
