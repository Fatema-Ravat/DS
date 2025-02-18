"""class LinkedList:
    def __init__(self,color):
        self.color =color
    def get_color(self):
        return self.color

l1 = LinkedList('red')
print(id(l1))
print(l1.get_color())"""

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def prepend(self,value):
        new_node = Node(value)
        if self.head is not None:
            #list is not empty
            new_node.next = self.head
            self.head = new_node
            
        else:
            self.head = new_node
            self.tail = new_node

        self.length = self.length +1

    def append(self,value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        
        self.length += 1
        return True
    
    def print_list(self):
        temp_node = self.head
        while temp_node is not None:
            print(temp_node.value)
            temp_node = temp_node.next
        
    def pop(self):
        if self.head is None:
            #empty list
            return None
        if self.head == self.tail:
            pop_node = self.head
            #only node in list
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            pop_node = temp_node.next
            temp_node.next = None
            self.tail = temp_node
            
        self.length -= 1
        return pop_node

    def pop_first(self):
        if self.length == 0:
            #list empty
            return None
        else:
            if self.head == self.tail:
                # only 1 node
                pop_node = self.head
                self.head =None
                self.tail = None
            else:
                pop_node = self.head
                self.head = self.head.next
            self.length -= 1
            return pop_node

    def get(self,index):
        if index <0 or index >= self.length:
            return False
        else:
            temp_node = self.head
            for _ in range(index):
                temp_node=temp_node.next
            return temp_node
        
    """def insert(self,index,value):
        if index < 0 or index > self.length:
            return False
        else:
            new_node = Node(value)
            if index==0:
                self.head = new_node
                self.tail = new_node
            else:
                temp_node = self.head
                temp_node_prev = self.head
                for _ in range(index):
                    temp_node_prev = temp_node
                    temp_node = temp_node.next
                temp_node_prev.next = new_node
                new_node.next = temp_node
                if index == self.tail:
                    self.tail = new_node
                self.length += 1
                return new_node
        
        #check the below more efficient fucntion for insert"""
    def insert(self,index,value):
        if index <0 or index>self.length:
            return False
        else:
            if index == 0:
                self.prepend(value)
            elif index == self.length:
                self.append(value)
            else:
                new_node = Node(value)
                temp_node = self.get(index -1)
                new_node.next = temp_node.next
                temp_node.next = new_node
                self.length += 1
            return True
        
    def remove(self,index):
        if index < 0 or index >= self.length:
            return None
        else:
            if index == 0:
                return self.pop_first()
            if index == self.length-1:
                return self.pop()
           
            temp_node_prev = self.get(index-1)
            temp_node = temp_node_prev.next

            temp_node_prev.next = temp_node.next
            temp_node.next = None
            self.length -=1
            return temp_node
        
    def reverse(self):
        if self.length >1:
            temp_node = self.head
            self.head = self.tail
            self.tail = temp_node

            temp_before = None
            temp_next = temp_node.next

            for _ in range(self.length):
                temp_next = temp_node.next
                temp_node.next = temp_before
                temp_before = temp_node
                temp_node = temp_next
        return True

           
            

        
    def set_value(self,index,value):
        """if index < 0 or index >= self.length:
            return False
        else:
            #temp_node = self.head
            #for _ in range(index):
            #    temp_node = temp_node.next

            #instead use the get method"""
        temp_node = self.get(index)
        if temp_node:
            temp_node.value = value
            return True
        return False

    def find_middle_node(self):
        if not self.head:
            return None
        if self.head == self.tail:
            return self.head
        
        slow = self.head
        fast = self.head
        
        while fast and  fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
    def has_loop(self):
        if self.head == self.tail:
            # no ll or only 1 element
            return False
        slow = self.head
        fast = self.head
        
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
            if slow == fast:
                return True
                
        return False   

    def partition_list(self,x):
        if self.length == 0:
            return None
        if self.length == 1:
            return True
        less = Node(0)
        greater = Node(0) 
        prev1 = less
        next1 = greater 
        temp = self.head

        while temp:
            if temp.value <x:
                less.next = temp
                less = temp
            else:
                greater.next = temp
                greater =temp
            
            print(temp.value)        
            temp = temp.next
            
        less. next = None
        greater.next = None 
        less.next = next1.next
        
        self.head = prev1.next
        
        return True

    def remove_duplicates(self):
        if self.length ==0 :
            return False
        
        prev = temp = self.head
        
        ll_set = set()
        
        while temp:
            if temp.value not in ll_set:
                ll_set.add(temp.value)
                prev = temp
            else:
                prev.next = temp.next
            
            temp = temp.next
            
        return True

    def binary_to_decimal(self):
        if self.length == 0:
             return 0
        temp = self.head
        dec_no = 0
        count = self.length-1
        
        while temp:
            if temp.value == 1:
                n1 = 2**count
                dec_no += n1
                
            count -=1
            temp = temp.next
            
        return dec_no
    
    def reverse_between(self,start,end):
        if self.length <=1 :
            return True
            
            
        dummy_node = Node(0)
        dummy_node.next = self.head
        prev = dummy_node
        
        for i in range(start):
            prev =prev.next
            
        current_node = prev.next

        l = end-start
        for _ in range(l):
            node_to_move = current_node.next
            current_node.next = node_to_move.next
            node_to_move.next = prev.next
            prev.next = node_to_move
        
        self.head = dummy_node.next
        
        return True
        


def find_kth_from_end(my_linked_list, k):
    if k<1:
        return None
    slow = my_linked_list.head
    fast = my_linked_list.head
    
    length =0
    while fast:
        length += 1
        fast = fast.next
    
    node_num = length-k
    print(node_num)
    if node_num <0:
        return None
    for _ in range(node_num):
        slow = slow.next
    
    return slow




my_ll = LinkedList(5)
my_ll.append(10)
my_ll.append(20)
my_ll.append(30)
my_ll.append(40)

my_ll.print_list()
my_ll.reverse_between(2,4)

my_ll.print_list()

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)
my_linked_list.reverse_between(2, 4)
my_linked_list.reverse_between(0, 4)
my_linked_list.reverse_between(3, 3)
my_linked_list.reverse_between(0, 0)


k = 7
#result = find_kth_from_end(my_linked_list, k)

#print(result.value)  # Output: 4


