import collections 
  

new_deque = collections.deque([1,2,3]) 
print(new_deque) 

n=int(input('Enter the number u want to append to the right : '))
new_deque.append(n) 
  
print ("The queue after appending at right is : ") 
print (new_deque) 
m=int(input('Enter the number u want to append to the left : '))
  
new_deque.appendleft(m) 
  
print ("The queue after appending at left is : ") 
print (new_deque) 
  
new_deque.pop() 
  
print ("The queue after deleting from right is : ") 
print (new_deque) 
  

new_deque.popleft() 
  

print ("The new_dequeque after new_deleting from left is : ") 
print (new_deque)
