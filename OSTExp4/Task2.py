a = list(map(int, input("Enter list 1 : ").split()))
b = list(map(int, input("Enter list 2 : ").split()))

print("Intersection of the 2 lists : ", list(filter(lambda x: x in a, b)))
