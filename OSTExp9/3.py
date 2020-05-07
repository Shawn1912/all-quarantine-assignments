import os

file1 = "File1.txt"
file2 = "File2.txt"
file3 = "File3.txt"

if os.path.isfile(file1 and file2):
    with open(file1) as f:
        content1 = f.read()
        print("File1 contains : ")
        print(content1)
    with open(file2) as f:
        content2 = f.read()
        print("\nFile2 contains : ")
        print(content2)
    with open(file3, 'w+') as f:
        f.write(content1 + '\n' + content2)
        f.seek(0)
        print("\nFile3 is created and it contains : ")
        print(f.read())
        
else:
    print(fileName + ' does not exist')
