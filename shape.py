def square(a):
    return(a*4)

def rectangle(a, b):
    return(2*a+2*b)

def triangle(a, b, c):
    return(a+b+c)

print("Please choose a shape")
print("1. square")
print("2. rectangle")
print("3. triangle")

choice=int(input("Enter a choice between 1, 2 and 3: "))



if choice==1:
    x=int(input("Enter the lenth of the square: "))
    ser= square(x)
    print("The circumference of the square is",ser)
elif choice==2:
    y=int(input("Enter the lenth of the rectangle: "))
    g=int(input("Enter the hieght of the rectangle: "))
    res= rectangle(y, g)
    print("The circumference of the rectangle is",res)
elif choice==3:
    e=int(input("Enter the 1st side of the shape: "))
    f=int(input("Enter the 2nd side of the shape: "))
    n=int(input("Enter 3rd side of the shape: "))
    ans= triangle(e, f, n)
    print("The circumference of the triangle is",ans)
    

else:
    print("Enter valid choice")





