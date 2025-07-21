#Enqueueu adds a new element in the queue
#dequeue removes and returns the first front element from the queueu
#peek returns the first element in the queue
#isEmpty checks if the queue is Empty
#size finds the number of the elements in the queue



queue = []

#Enququ

queue.append('A')
queue.append("B")
queue.append('C')

print("Peek", queue)

#peek

frontElement = queue[0]
print("Peek", frontElement)

#Dequeue

poppedElement = queue.pop(0)
print("Dequeue:", poppedElement)

#size 
print("size", len(queue))
















