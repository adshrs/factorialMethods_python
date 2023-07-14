# Method 2(For loop)

# Defining function that calculates the factorial of number 'n' 
def factorial(n):
    if n == 0:
        return 1
    
    x = 1
    
    for i in range(1, n+1):
        x = x * i
        
    return x   


# Asking user for a number to initiate calculation
x = int(input('Calculate factorial of: '))

# Printing the factorial of the user's input
print(factorial(x))