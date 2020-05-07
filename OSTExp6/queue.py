from queue import Queue 
  
# Initializing a queue 
q = Queue(maxsize = 3) 
  
print('The size of the queue is {}'.format(q.qsize()))  
  
# Adding of element to queue 
print('Adding elements to the queue')
print(q.put('m')) 
print(q.put('b')) 
print(q.put('a')) 
  

print("\nIs queue Full: ", q.full())  
  
# Removing element from queue 
print("\nElements dequeued from the queue") 
print(q.get()) 
print(q.get()) 
print(q.get()) 
  
print("\nIs queue Empty: ", q.empty()) 
print("Adding '1' to the queue") 
q.put(1) 
print("\nEmpty: ", q.empty())  
print("Full: ", q.full())
