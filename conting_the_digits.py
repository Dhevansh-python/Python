x=int(input("Enter a number for me to count the digits in the number: "))
y=x
c=0

while x!=0:
    x=x//10
    c=c+1

print("The number of digits in  ",y,"is ", c)
