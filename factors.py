import math
start = 1
num = int(input("Enter a value: "))

new_stop = int(math.sqrt(end))+1

factor_count = 0
while start < new_stop:
    if num%start == 0:
        dividend = num // start
        if start != dividend:
            factor_count += 2
        else:
            factor_count += 1
    start += 1
print(num + " has " + factor_count + " factors")

'''
num = int(input("enter a number: "))
i = 1
while i<=num:
    if num%i==0:
        print(i)
    i+=1
'''