# Write a Python program to print the first n Fibonacci numbers.
# Example for n = 7: 0 1 1 2 3 5 8


def sequence(n):

    a, b = 0 ,1

    for _ in range(n):
        print(a,end=" ")
        a,b= b ,b+a

print(sequence(7))