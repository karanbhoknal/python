# Find the sum of all even Fibonacci numbers below 4 million 
def fibo_even(limit):
    a , b =0, 1

    total=0

    while a<limit:
        if a%2==0:
            total +=a  
        a,b=b,b+a
    
    return total

print(fibo_even(4000000))  # Output: 4613732
