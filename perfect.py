# here write the python program to write perfect number
n = int(input("Enter the number: ")) 
if n <= 0:
    print("Please enter a positive integer.")
else:
    sum_of_divisors = 0

    for i in range(1, n):
        if n % i == 0:
            sum_of_divisors += i

    if sum_of_divisors == n:
        print("The provided number is a perfect number.")
    else:
        print("The number is not a perfect number.")