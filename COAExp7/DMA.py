name=["Process P1","Free space 1","Process P2","Free space 2","Process P3","Free space 3"]
mem=[3,4,6,5,1,2]

def printTable():
    global name,mem
    print("Content\t\tSize")
    print("====================")
    for (x,y) in zip(name,mem):
        print("{}\t{}K\t".format(x,y))
    
def inputs():
    global m
    print()
    m=int(input("Enter the size of Process P4 : "))
    print()
    print()
    print("1. First Fit")
    print("2. Best Fit")
    print("3. Next Fit")
    print("4. Worst Fit")
    print()
    global ch
    ch=int(input("Enter your choice : "))
    print()

def choice():
    global ch
    if(ch==1):
        firstFit()
    if(ch==2):
        bestFit()
    if(ch==3):
        nextFit()
    if(ch==4):
        worstFit()

def firstFit():
    t=0
    global name,mem,m
    for (x,y) in zip(name,mem):
        if(x[0]=='F'):
            if y>=m:
                break
        t=t+1
    name.insert(t,"Process P4")
    mem.insert(t,m)
    mem[t+1]=mem[t+1]-m
    if mem[t+1]==0:
        del mem[t+1]
        del name[t+1]

def swap(list, pos1, pos2): 
      
    list[pos1], list[pos2] = list[pos2], list[pos1] 
    return list

def nextFit():
    t=0
    global name,mem,m
    name.reverse()
    mem.reverse()
    for (x,y) in zip(name,mem):
        if(x[0]=='F'):
            if y>=m:
                break
        t=t+1
    name.insert(t,"Process P4")
    mem.insert(t,m)
    mem[t+1]=mem[t+1]-m
    if mem[t+1]==0:
        del mem[t+1]
        del name[t+1]
    else:
        swap(name,t,t+1)
        swap(mem,t,t+1)
    name.reverse()
    mem.reverse()

def bestFit():
    global name,mem,m
    t=1000
    for (x,y) in zip(name,mem):
        if(x[0]=='F'):
            if y>=m and y<t:
                t=y
    t=mem.index(t)
    name.insert(t,"Process P4")
    mem.insert(t,m)
    mem[t+1]=mem[t+1]-m
    if mem[t+1]==0:
        del mem[t+1]
        del name[t+1]

def worstFit():
    global name,mem,m
    t=-1000
    for (x,y) in zip(name,mem):
        if(x[0]=='F'):
            if y>=m and y>t:
                t=y
    t=mem.index(t)
    name.insert(t,"Process P4")
    mem.insert(t,m)
    mem[t+1]=mem[t+1]-m
    if mem[t+1]==0:
        del mem[t+1]
        del name[t+1]
    
printTable()
inputs()
choice()
printTable()
