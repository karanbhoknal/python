# Write a program to print Fibonacci numbers less than 100

def fibo(n):

    a,b =0,1

    while a<n:
        print(a,end=" ")

        a,b = b,b+a

print(fibo(100))  # Output: 0 1 1 2 3 5 8 13 21 34 55 89