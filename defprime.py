# check the number is prime or not using function

def prime(n):
   
    
    for i in range(2,n):
        if n%i==0:
            print("is not prime")
                
    else:
        print("is prime")
n=int(input("enter the number:"))
prime(n)
                  