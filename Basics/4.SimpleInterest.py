#Program to Calculate Simple Interest

principal = float(input(" Please Enter The Principal Amount : " ))
rate = float(input(" Please Enter The Rate Of Interest Per Annum  : " ))
time = float(input(" Please Enter The Time Period in Years  : " ))
simpleInterest = (principal * rate * time ) / 100
amount = principal + simpleInterest
print(f' The Simple Interset of the Principal Amount of {principal} at the Rate of {rate} Per Annum for the Time of {time} Year(s) = {simpleInterest} ')
print(f' Total Amount = {amount} ')
