# Write a function to check whether a given number is a Fibonacci number or not.
# Example: 13 → Yes, 14 → No.

def is_fibonacci(n):

    a,b =0,1

    while a<n:
        a, b = b, b+a

    return a==n

print(is_fibonacci(13))  # Output: True
print(is_fibonacci(14))  # Output: False