def factorial(x):
#def defines factorial which factorial is a function and x is the parameter
    """the function is being defined andit wil be called many times"""

    
    if x==0 or x==1:
        return 1
    
    else:
        x*factorial(x-1)

print(factorial.__doc__)

print("The factorial of 0: ", factorial(0))
print("The factorial of 0: ", factorial(1))
print("The factorial of 0: ", factorial(2))
print("The factorial of 0: ", factorial(5))
print("The factorial of 10: ", factorial(10))
