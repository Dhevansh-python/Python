def sub(a,b):
    print(a-b)

def mul(a,b):
    print(a*b)

def div(a,b):
    print(a/b)




def add(a,b):
    print(a+b)

a=int(input("Enter a number: "))
b=int(input("Enter another number: "))
print("Press \n1.addition\n2.subtraction\n3.multyplication\n4.division")
op=int(input("Enter your choice: "))
if op==1:
    add(a,b)

elif op==2:
    sub(a,b)

elif op==3:
    mul(a,b)

elif op==4:
    div(a,b)

else:
    print("Enter either 1,2,3 or 4")