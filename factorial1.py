# Method 1(While loop)

# Defining function that calculates the factorial of number 'n' 
def factorial(n):
    if n == 0:
        return 1
    
    i = 0
    f = 1

    while i < n:
        i = i + 1
        f = f * i
    
    return f


# Asking user for a number to initiate calculation
x = int(input('Calculate factorial of: '))

# Printing the factorial of the user's input
print(factorial(x))
