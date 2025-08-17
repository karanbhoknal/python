# Find the sum of the first n Fibonacci numbers.
# Example for n = 5: 0 + 1 + 1 + 2 + 3 = 7

def sum_fibo(n):

    a, b =0,1

    total=0 

    for i in range(n):
        total=total+a
        a, b =b,b+a

    return total

print(sum_fibo(5))  # Output: 7