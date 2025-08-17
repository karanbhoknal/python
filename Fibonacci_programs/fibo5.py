# Write a recursive function to print the Fibonacci series up to n terms.
def fibonacci_recursive(n):
    if n <= 1:
        return n
    return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Print first 7 numbers
for i in range(7):
    print(fibonacci_recursive(i), end=" ")


