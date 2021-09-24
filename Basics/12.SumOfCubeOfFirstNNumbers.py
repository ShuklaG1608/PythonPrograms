#Program To Print Sum of Cube of First 'N' Natural Number

num = int(input(" Please Enter The Value of Number Till Where SUM Is Required : "))
SUM = 0
for i in range(1,num+1):
    SUM = SUM + (i ** 3)
print(f' The Sum of Cube of First {num} = {SUM} ' )
