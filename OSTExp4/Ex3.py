l = [1,10,2,9,6,99,20,100,11,33]
def iseven(num):
    if num % 2 == 0:
        return True
    else:
        return False
newlist = filter(iseven, l)

for i in newlist:
    print(i)
