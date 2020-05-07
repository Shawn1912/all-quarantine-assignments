x = lambda a : a + 10
print(x(5))


adder = lambda x, y: x + y
print (adder (1, 2))



x="Computer Dept."
(lambda x : print(x))(x)

y = (lambda x : print(x))
y(x)



print(y("Computer Dept."))

# Initialize a list of numbers (odd
#& even) and need to filter out only the even numbers
#in it
a = [1,2,3,4,5,6,7,8,9,0]

even = list(filter(lambda x: x % 2 == 0, a))
print(even)

odd = list(filter(lambda x:x % 2 != 0, a))
print(odd)
