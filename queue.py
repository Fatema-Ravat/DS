class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    # in Queue you add at the last(tail end) and 
    # remove from the head end of LinkedList this way both operation is O(1)
     
    def enqueue(self,value):
        new_node = Node(value)
        if self.length == 0:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node

        self.length +=1
        return True

    def dequeue(self):
        if self.length==0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = temp.next
            temp.next = None
        self.length -=1
        return temp

class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []
        
    def enqueue(self,value):
        if len(self.stack1) == 0:
            self.stack1.append(value)
            print("in first if")
        else:
            print(self.stack1)
            while len(self.stack1)>0:
                self.stack2.append(self.stack1.pop())
                print("in first whiel:", self.stack2)
                
            
            self.stack1.append(value)
            print(self.stack1 , "new val added")
            while len(self.stack2) >0:
                self.stack1.append(self.stack2.pop())
                print("in second whiel:", self.stack1)


    def dequeue(self):
        if len(self.stack1) == 0:
            return None
        else:
            
            temp = self.stack1.pop()            
            return temp
            

    def peek(self):
        return self.stack1[-1]

    def is_empty(self):
        return len(self.stack1) == 0
        
        

# Create a new queue
q = MyQueue()

# Enqueue some values
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

# Output the front of the queue
print("Front of the queue:", q.peek())

# Dequeue some values
print("Dequeued value:", q.dequeue())
print("Dequeued value:", q.dequeue())

# Output the front of the queue
print("Front of the queue:", q.peek())

# Check if the queue is empty
print("Is the queue empty?", q.is_empty())


"""
    EXPECTED OUTPUT:
    ----------------
    Front of the queue: 1
    Is the queue empty? False
    
"""
