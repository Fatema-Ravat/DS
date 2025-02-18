class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self,value):
        n= Node(value)
        self.head = n
        self.tail = n
        self.length = 1

    def append(self,value):
        n= Node(value)
        if self.length == 0:
            self.head = self.tail = n
        else:
            temp =self.tail
            self.tail = n
            temp.next = n
            n.prev = temp
        self.length +=1

        return True
    
    def pop(self):
        if self.length == 0:
            return None
        
        temp = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
           
        else:
            self.tail = temp.prev
            self.tail.next = None
            temp.prev = None
        self.length -= 1
        return temp
            
    def prepend(self,value):
        n = Node(value)
        if self.length == 0:
            self.head = n
            self.tail = n
        else:
            temp = self.head
            self.head.prev = n
            n.next = temp
            self.head = n
        self.length +=1
        return True
    
    def pop_first(self):
        if self.length == 0:
            return None
        temp = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = temp.next
            temp.next = None
            self.head.prev = None

        self.length -=1
        return temp 
    
    def get(self,index):
        if self.length == 0 or index > self.length or index < 0:
            return None
        
        if index < self.length/2 : 
            print("in first half")
            temp = self.head
            for _ in range(index):
                temp = temp.next
        else:
            print("in second half",self.length-index)
            temp = self.tail
            for _ in range(self.length - index-1):
                temp= temp.prev
                print(temp.value)

        return temp
    def set_value(self,index,val):
        '''if index <0 or index> self.length:
            return False
        if self.length == 0:
            return False
        if index < self.length/2 :
            temp = self.head
            for _ in range(index):
                temp = temp.next
            temp.value = val
        else:
            temp = self.tail
            for _ in range(self.length-index -1):
                temp = temp.prev'''
        temp = self.get(index)
        if temp:
            temp.value = val
            return True
        return False
    
    def insert(self,index,value):
        if index < 0 or index > self.length:
            return None
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        
        n = Node(value)
        temp = self.get(index-1)
        after = temp.next

        after.prev = n
        n.next = after

        temp.next = n
        n.prev = temp

        self.length +=1

        return True
    
    def remove(self,index):
        if index <0 or index >self.length-1:
            return None
        
        if index == 0:
            return self.pop_first()
        if index == self.length-1:
            return self.pop()
        
        temp = self.get(index)

        before = temp.prev
        after = temp.next

        before.next = after
        after.prev = before

        temp.next = temp.prev = None

        self.length -=1

        return temp
    
    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def swap_first_last(self):
        # you dont swap the pointers, just swap the value :)
        if self.length == 0:
            return False
            
        if self.head == self.tail:
            return True
            
        temp = self.head.value
        self.head.value = self.tail.value
        self.tail.value = temp
        
        return True
    def reverse(self):
        # swap the prev and next pointer and head and tail
        if self.length == 0:
            return True
        if self.head == self.tail:
            temp_head = self.head
            self.head = self.tail
            self.tail = temp_head
            return True
            
        temp = self.head
        
        for _ in range(self.length):
            temp_pointer = temp.next
            
            temp.next = temp.prev
            temp.prev = temp_pointer
            
            temp = temp_pointer
            
        
        temp_head = self.head
        self.head = self.tail
        self.tail = temp_head
        
            
        return True
      
    def is_palindrome(self):
        # compare values till half the list
        if self.length == 0:
            return True
        if self.head == self.tail:
            return True
            
        n = (int)(self.length/2)
        
        front = self.head
        back = self.tail
        
        for _ in range(n):
            
            if not front.value == back.value:
                return False
            front = front.next
            back = back.prev
            
        return True

    def swap_pairs(self):
        if self.length <=1:
            return True
        
        first = self.head

        self.head =self.head.next

        n = (int)(self.length/2)
        for _ in range(n):
            second = first.next
            print(first.value,second.value , "in loop before first,second")

            temp_prev = first.prev
            temp_next = second.next

            second.next = first
            first.prev = second


            second.prev = temp_prev
            first.next = temp_next

            if temp_prev:
                temp_prev.next = second
            if temp_next:
                temp_next.prev = first
            
            self.print_list()
            first = second.next.next
        
        
        return True
        


my_doubly_linked_list = DoublyLinkedList(1)
my_doubly_linked_list.append(2)
my_doubly_linked_list.append(3)
my_doubly_linked_list.append(4)
my_doubly_linked_list.append(5)
my_doubly_linked_list.append(6)



print('DLL before :')
my_doubly_linked_list.print_list()
my_doubly_linked_list.swap_pairs()

print('DLL after :')
my_doubly_linked_list.print_list()
#print(my_doubly_linked_list.is_palindrome())