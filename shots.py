try:
    shots=int(input("Enter how much shots have been taken: "))
    goals=int(input("Enter how much goals have been scored: "))

    res=(goals/shots)
    print("your shot rate is", res)

except ZeroDivisionError:
    print("The shots cannot be 0")

except ValueError:
    print("Enter a valid number")

finally:
    print("Thank you for using the penalty shootout game")












    res=(shots-goals)



































'''You are building a football penalty shootout program. The user enters the number of penalty shots taken and goals scored.

👉 Write a program that:

Takes shots and goals as input

Calculates goal success rate (goals / shots)

Handles these errors:

If user enters text → show error

If shots = 0 → handle division error'''