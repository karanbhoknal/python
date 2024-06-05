n=int(input("enter the number:"))
z=n
sum=0
while(n>0):
    sum=sum+(n%10)*(n%10)*(n%10)
    n=n//10

if(sum==z):
    print("number is armstrong")
else:
    print("number is not armstrong")