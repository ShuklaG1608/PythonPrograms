#Program To Check For Armstrong Number

num = input(" Enter The Number : " )
length = len(num)
numInteger = int(num)
temp = numInteger
SUM = 0
while(numInteger != 0):
    remainder = numInteger % 10
    SUM = SUM + (remainder ** length)
    numInteger = numInteger // 10

if(SUM == temp):
    print(f' {temp} is An Armstrong Number ' )
else:
     print(f' {temp} is Not An Armstrong Number ' )
