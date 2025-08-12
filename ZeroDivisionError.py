# write function that takes 2 numbers nad return their division use try and except block to handle division error by zero
def string(a,b):

  try:
    return a/b

  except ZeroDivisionError:
    return "can not divide by zero"

print(string(10,0))
print(string(12,6))