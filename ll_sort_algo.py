class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
        
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def my_merge(self,ll2):
        dummy = Node(0)
        dummy.next = self.head
        parent = dummy
        i = self.head
        j = ll2.head
        
        while i is not None and j is not None:
            if j.value <= i.value:
                #if new list value less than only add
                parent.next = j
                temp = j.next
                j.next = i
                parent = j
                j=temp
                
            else:
                parent = i
                i= i.next

        if j is not None:
            parent.next = j
            self.tail = ll2.tail

        self.length = self.length + ll2.length

        
        self.head = dummy.next
        

    def merge(self, other_list):
        other_head = other_list.head
        dummy = Node(0)
        current = dummy
 
        while self.head is not None and other_head is not None:
            if self.head.value < other_head.value:
                current.next = self.head
                self.head = self.head.next
            else:
                current.next = other_head
                other_head = other_head.next
            current = current.next
 
        if self.head is not None:
            current.next = self.head
        else:
            current.next = other_head
            self.tail = other_list.tail
 
        self.head = dummy.next
        self.length += other_list.length
          
    


l1 = LinkedList(1)
l1.append(2)
l1.append(3)
l1.append(5)



l2 = LinkedList(3)
l2.append(4)
l2.append(7)
l2.append(8)

l1.my_merge(l2)

l1.print_list()


"""
    EXPECTED OUTPUT:
    ----------------
    1 
    2 
    3 
    4 
    5 
    6 
    7
    8

"""