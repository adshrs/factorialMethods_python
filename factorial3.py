# Method 3(Recursion)

# Defining function that calculates the factorial of number 'n' 
def factorial(n):
    if n == 0:
        return 1
    
    result = n * factorial(n - 1)
    
    return result


# Asking user for a number to initiate calculation
x = int(input('Calculate factorial of: '))

# Printing the factorial of the user's input
print(factorial(x))