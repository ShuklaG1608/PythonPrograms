#Program To Print All Prime Number in The Given Range

startNum = int(input(" Enter The Start Number From Where To Be Checked For : "))
endNum = int(input(" Enter The Last Number Till Where To Be Checked For : "))
if(startNum == endNum or startNum > endNum):
    print(f' There is no Prime Number between {startNum} and {endNum} . ')
else:
    for num in range(startNum,endNum+1):  
        if(num == 0 or num == 1):
            print(f' There is no Prime Number between {startNum} and {endNum} . ')
        else:
            for i in range(2,num//2+1):
                if(num % i == 0):
                    break
            else:
                print(num)
       
