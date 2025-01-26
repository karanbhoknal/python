# write the python program to check number is perfect or not using function

def perfect(n):
    count=0

    for i in range(1,n):
        if n%i==0:
            count=count+1
# if statement execute the code if condition is true
        if count==2:
            print("the number is prefect")
            
# if statement execute the code if condition is false
        else:
            print("the number is not perfect")
          
# main functions
n=int(input("Enter the perfect number:"))
perfect(n)