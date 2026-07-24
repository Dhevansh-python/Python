try:
    age=int(input("Enter your age: "))

    
except ValueError:
    print("Please Enter a valid age")

finally:
    print("Thank you for using the age-checker")


