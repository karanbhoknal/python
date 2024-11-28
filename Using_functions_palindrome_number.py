
# write a python program to check number is palindrome or not using function in python

def palindrome(n):
    z=n
    rev=0

    while (z>0):
        rev=rev*10+z%10
        z=z//10

    if rev==n:
        print("palindrome")
    
    else:
        print("not palindrome")

# main functions
n=int(input("Enter the number :"))
palindrome(n)