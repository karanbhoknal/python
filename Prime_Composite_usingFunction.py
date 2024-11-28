
# writ python program to check number is prime or composite and nither prime or composite by using function


def primecompo(n):
    count=0

    for i in range(1,n+1):
        if n%i==0:
            count=count+1
        i=i+1

        if count==2:
            print("prime")
        elif count>2:
            print("composite")
        
        else:
            print("nither prime or composite")


# main function
n=int(input("Enter the number:"))
primecompo(n)