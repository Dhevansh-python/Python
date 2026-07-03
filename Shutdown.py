

def shutdown (condition1):
    if condition1=="yes":
       return("Shuting down")
        
    elif condition1=="no":
        return("Abort shutdown")
    
    else:
        return("Sorry")

x=(input("Are you done with your work: "))

res = shutdown(x)
print(res)