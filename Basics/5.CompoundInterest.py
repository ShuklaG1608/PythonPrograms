#Program to Calculate Compound Interest

principal = float(input(" Please Enter The Principal Amount : " ))
rate = float(input(" Please Enter The Rate Of Interest Per Annum  : " ))
time = float(input(" Please Enter The Time Period in Years  : " ))
amount = principal * ((1 + (rate/100))**time)
compundInterest = amount - principal
print(f' The Compound Interset of the Principal Amount of {principal} at the Rate of {rate} Per Annum for the Time of {time} Year(s) = {compundInterest} ')
print(f' Total Amount = {amount} ')
