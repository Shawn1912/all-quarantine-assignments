import os
fileName = "File1.txt"
if os.path.isfile(fileName):
    f = open(fileName, 'r')
    for x in f:
        print(x.rstrip())
    f.close()

    f = open(fileName, 'a')
    n = int(input("\nEnter number of lines to be appended : "))
    for i in range(0, n):
        string = input("Enter string to be appended : ")
        f.write('\n' + string)
    f.close()

    newName = 'changed.txt'
    os.rename(fileName, newName)
    f = open(newName, 'r')
    print()
    print(f.read())
    f.close()
else:
    print(fileName + ' does not exist')

#os.rename('TestDirectory')
