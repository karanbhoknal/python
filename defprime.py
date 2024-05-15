# check the number is prime or not using function

def prime(n):
   count=0
    
    for i in range(1,n+1):
        if n%i==0:
           count=count+1
   if(count==2):
      
         print("Number is prime")
                
    else:
        print("number is not prime")
n=int(input("enter the number:"))
prime(n)
                  
