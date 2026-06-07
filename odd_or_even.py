num=int(input("Enter the total numbers of number: "))
res=0


for i in range(1, num+1):

    n=int(input(f"Enter number {i}, :" ))

    if n%2==0:
        res=res+n
    else:
        res=res-n
    i=i+1

print ("the result of numbers", res)

