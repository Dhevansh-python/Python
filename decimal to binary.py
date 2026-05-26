num=int(input("Enter a number to convet to a binary: "))

newmod=''

while num>0:
    mod=num%2
    num=num//2
    newmod=str(mod)+newmod

print("The binary value of ",num,"is ",newmod)
