class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height =1
# in stack push and pop at the head of the LinkedList

    def print_stack(self):
        if self.height >0:
            temp = self.top
            while temp:
                print(temp.value)
                temp = temp.next


    def push(self,value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.height +=1
        return True
    
    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = temp.next
        temp.next = None
        self.height -=1
        return temp
    
class StackList:
    def __init__(self):  
        self.stack_list = []

    def print_stack(self):
        for i in range(len(self.stack_list)-1,-1,-1):
            print(self.stack_list[i])
    
    def is_empty(self):
        return len(self.stack_list) == 0
    
    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack_list[-1]
    
    def push(self,value):
        self.stack_list.append(value)
    
    def pop(self):
        if len(self.stack_list) == 0:
            return None
        return self.stack_list.pop()
    

def is_balanced_parentheses(s):   
    open_counter =0
    closed_counter = 0
    counter = 0 
    for x in s:
        if x == '(':
            open_counter +=1
            counter +=1
        if x== ')':
            if closed_counter<=open_counter and not open_counter == 0: # ==0 is test for first character is )
                closed_counter+=1
                counter -=1
            else:
                return False
        
    print("counter:",counter)
    if counter ==0:
        return True
    else:
        return False
    

'''def is_balanced_parentheses(parentheses):
    stack = Stack()
    for p in parentheses:
        if p == '(':
            stack.push(p)
        elif p == ')':
            if stack.is_empty() or stack.pop() != '(':
                return False
    return stack.is_empty()'''

def reverse_string(s):
    st = StackList()
    
    for x in s:
        st.push(x)
    
    new_string = ""
    
    while not st.is_empty():
        new_string = new_string + st.pop()
        
    return new_string

def sort_stack(in_st):
    
    sort_st = StackList()
    
    while not in_st.is_empty():
        x= in_st.pop()
        if sort_st.is_empty():
            sort_st.push(x)
        else:
            if   x > sort_st.peek():
                sort_st.push(x)
            else:
                count = 0
                while  not sort_st.is_empty() and sort_st.peek() > x:
                    temp = sort_st.pop()
                    count +=1
                    in_st.push(temp)
                    

                sort_st.push(x)
                for _ in range(count):
                    sort_st.push(in_st.pop())

        
    while not sort_st.is_empty():
        in_st.push(sort_st.pop())

        
my_stack = StackList()
my_stack.push(3)
my_stack.push(1)
my_stack.push(5)
my_stack.push(4)
my_stack.push(2)

print("Stack before sort_stack():")
my_stack.print_stack()

sort_stack(my_stack)

print("\nStack after sort_stack:")
my_stack.print_stack()




