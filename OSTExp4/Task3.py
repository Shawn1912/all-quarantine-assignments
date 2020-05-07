a = list(map(int, input("Enter list 1 : ").split()))
b = list(map(int, input("Enter list 2 : ").split()))

print("Addition : ",list(map(lambda x,y: x+y, a, b)))
