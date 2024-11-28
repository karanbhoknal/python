# check the number is prime or not using function

def prime(n):

   count=0
   for i in range(1,n+1):
      if n%i==0:
         count=count+1
         i=i+1
      if count==2:
         print(" This is prime number:")
      else:
         print("This is not prime number:")
         
#Main functions

n=int(input("Enter the number:"))
prime(n)
                  
