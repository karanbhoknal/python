# Write a function to return the nth Fibonacci number using iteration (not recursion).
# Example: If n = 5, output should be 3.

def fibo(n):
    a,b =0 ,1

    for _ in range(n-1):
        a,b =b,b+a

    return a

print(fibo(5))