#A stack is a data structure that can hold many elements, and 
#the last element added is the first one to be removed.


stack=[]

#push
stack.append("A")
stack.append("B")
stack.append("C")
stack.append("D")

print("Stack:", stack)

#peek
#the last element to be added LIFO
topElement = stack[-1]
print("Peek:", topElement)

#Pop
poppedElement = stack.pop()
print("Pop:", poppedElement)

#let me check the stack
print(stack)
#ive notted that d is no longer in the stack

#isEmpty
isEmpty = not bool(stack)
print("isEmpty", isEmpty)  
#the stack is not empty the output is false

#size
print("Size", len(stack))
#returns 3













