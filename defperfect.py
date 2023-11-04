def perfect(n):
    sum_of_divisor=0
    
    
    for i in range(1,n):
        if n%i==0:
            sum_of_divisor=sum_of_divisor + i
        
    if(sum_of_divisor==n):
        print(f"is a perfect  number")

    else:
        print(f"is  not perfect  number")

n=int(input("enter the number:"))
perfect(n)