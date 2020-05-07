from functools import reduce
a = list(map(int, input("Enter list : ").split()))

print("Sum is : ", reduce(lambda x,y: x+y, a))
