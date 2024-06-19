#Program to find odd number between 40 to 55 and thier sum.
x = 40
sum = 0
while(x >= 40 and x <= 55):
    if(x%2 == 1):
        print(x)
        sum += x
    x += 1
else:
    print("sum is",sum)        
