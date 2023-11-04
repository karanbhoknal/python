#In this program removing the 0 digit using python code

list=[2303,43058,908,8903]
output=[]

for num in list:
      num=str(num)
      new=num.split('0')
      output.append(int("".join(new)))
print(output)