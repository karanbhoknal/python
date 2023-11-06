

# Addition of  even numbers in list

list=[1,2,3,4,5,6]
sum=0
for i in list:
    if i%2==0:
        sum=sum+i
        print(i)
print("addition of even number:",sum)