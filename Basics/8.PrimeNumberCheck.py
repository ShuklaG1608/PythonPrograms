num = int(input(" Enter The Number To Be Checked For : "))
if(num == 0 or num == 1):
    print(f' {num} is NOT a Prime Number. ')
else:
    prime = True
    for i in range(2,num//2+1):
        if(num % i == 0):
            prime = False
        else:
            prime = True
    if(prime == True):
        print(f' {num} is a Prime Number. ')
    else:
        print(f' {num} is NOT a Prime Number. ')
            
        
