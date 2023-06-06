
# Using Loop 
num = int(input("Enter a  number: "))
factorial = 1
if num < 0:
    print("The factorial cannot be negative")
elif num == 0:
    print("The factorial of 0 is 1")
else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("The factorial of",num,"is",factorial)                



# Using Recursion    
def factorial(x):
    if x == 1:
        return x
    else:
        return (x * factorial(x-1))
    
num = int(input("Enter the number: "))
result = factorial (num)
print("The factorial of",num,"is",result)    
    

