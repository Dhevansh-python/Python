paid=int(input("Enter how much you paid the shopkeeper: "))
topay=int(input("Enter how much you had to pay: "))

res=(paid-topay)

if res<0:
    print(f"You still have to pay {res}!")  

elif res>=0:
    print("The shopkeeper still has to pay you", res)        

else:
    print("Please enter a valid number")


