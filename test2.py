def add(a,b):
    print(a+b)




def sub(a,b):
    
    print(a-b)




def mul(a,b):
    print(a*b)


def div(a,b):
    print(a/b)
try:
    a=int(input("Enter your number: "))
    b=int(input("Enter another number: "))
    print("1.add\n2.subtract\n3.multiply\n4.divide: ")
    cal=int(input("Enter what arthemtic operation do you wan't to use: "))

    if cal==1:
        add(a,b)
    elif cal==2:
        sub(a,b)
    elif cal==3:
        mul(a,b)
    elif cal==4:
        div(a,b)
    else:
        print("Please choose a number between 1-4")

except ValueError:
    print("please Enter a valid integer")

except ZeroDivisionError:
    print("The denominator cannot be 0")





