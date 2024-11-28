n=int(input("Enter the number is perfect or not"))
count=0

for i in range(1,n):
    if n%i==0:
        count=count+1
    i=i+1

if count==2:
    print("The provided number is perfect")

else:
    print("The provide number is not perfect")
    
