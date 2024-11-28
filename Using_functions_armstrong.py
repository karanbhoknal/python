#  write a python program to check number is armstrong  or not using function in python

def arm(n):

    sum=0
    z=n
    while(n>0):
        sum=sum+(n%10)*(n%10)*(n%10)
        n=n//10

    if sum==z:
        print("armstrong")
    else:
        print("not armstrong")
# main function
n=int(input("Enter the number:"))
arm(n)