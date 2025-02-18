class MaxHeap:
    # this type of heap has always the parent node greater than child nodes.
    def __init__(self):
        self.heap = []

    #heap helper methods

    def _left_child(self,index):
        #gives the index of the left child of input node index
        return 2*index + 1
    
    def _right_child(self,index):
        #gives the index of the right child of the input node index
        return 2*index + 2
    
    def _parent_index(self,index):
        # returns the index of the parent node
        return (index -1)//2
    
    def _swap(self,index1,index2):
        # temp = self.heap[index1]
        # self.heap[index1] = self.heap[index2]
        # self.heap[index2] = temp
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def _sink_down_old(self,index):
        
        current =index
        heap_len = len(self.heap)

        while True:
            if heap_len>self._left_child and self.heap[self._left_child(current)] > self.heap[current] and self.heap[self._left_child(current)] > self.heap[self._right_child(current)]:
                self._swap(current,self._left_child)
                current = self._left_child
            elif heap_len>self._right_child and self.heap[self._right_child(current)] > self.heap[current] and self.heap[self._right_child(current)] > self.heap[self._left_child(current)]:
                self._swap(current,self._right_child)
                current = self._right_child
            else:
                break

    def _sink_down(self,index):
        current = index
        heap_len = len(self.heap)

        while True:
            left_index = self._left_child(current)
            right_index = self._right_child(current)

            if (left_index < heap_len and self.heap[left_index] > self.heap[current]):
                current = left_index
            if (right_index < heap_len and self.heap[right_index] > self.heap[current]):
                current = right_index
            if current != index :
                self._swap(current,index)
                index = current
            else:
                return
            

    def print_heap(self):
        for i in range(len(self.heap)):
            print(self.heap[i])
    
        
    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap)-1

        while current >0 and self.heap[current] > self.heap[self._parent_index(current)]:
            self._swap(current,self._parent_index(current))
            current = self._parent_index(current)

        return True
    
    def remove(self):
        # if no item in heap
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        
        return_val = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)

        return return_val

    
class MinHeap:
    def __init__(self):
        self.heap = []
    
    def _left_index(self,index):
        return (2*index)+1
    
    def _right_index(self,index):
        return (2*index)+2
    
    def _parent(self,index):
        return (index-1)//2

    def _swap(self,index1,index2):
        self.heap[index1],self.heap[index2] = self.heap[index2],self.heap[index1]

    def print_heap(self):
        print(self.heap)

    def insert(self,value):
        self.heap.append(value)
        current = len(self.heap) -1

        while current>0 and self.heap[current] < self.heap[self._parent(current)]:
            self._swap(current,self._parent(current))
            current = self._parent(current)

        return True
            

    def remove(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        return_val = self.heap[0]
        self.heap[0] = self.heap.pop()

        self._sink_down(0)
        return return_val
    
    def _sink_down(self,index):
        current_index = index
        heap_len = len(self.heap)

        while True:
            left_index = self._left_index(current_index)
            right_index = self._right_index(current_index)

            if (left_index < heap_len and self.heap[current_index] > self.heap[left_index]):
                current_index = left_index
            if (right_index < heap_len and self.heap[current_index] > self.heap[right_index]):
                current_index = right_index
            if current_index != index:
                self._swap(current_index,index)
                index = current_index
            else:
                return


def find_kth_smallest(nums,k):
    
    myheap = MaxHeap()
    for i in range(len(nums)):
        myheap.insert(nums[i])
        
    heap_len = len(nums)
    
    for _ in range(heap_len-k):
        myheap.remove()
        
    return myheap.remove()

def stream_max(nums):
    
    myheap = MaxHeap()
    
    return_list = []
    
    for i in range(len(nums)):
        myheap.insert(nums[i])
        return_list.append(myheap.heap[0])
    
    return return_list


"""
nums = [[3,2,1,5,6,4], [6,5,4,3,2,1], [1,2,3,4,5,6], [3,2,3,1,2,4,5,5,6]]
ks = [2, 3, 4, 7]
expected_outputs = [2, 3, 4, 5]

for i in range(len(nums)):
    print(f'Test case {i+1}...')
    print(f'Input: {nums[i]} with k = {ks[i]}')
    result = find_kth_smallest(nums[i], ks[i])
    print(f'Output: {result}')
    print(f'Expected output: {expected_outputs[i]}')
    print(f'Test passed: {result == expected_outputs[i]}')
    print('---------------------------------------')

"""


test_cases = [
    ([], []),
    ([1], [1]),
    ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),
    ([1, 2, 2, 1, 3, 3, 3, 2, 2], [1, 2, 2, 2, 3, 3, 3, 3, 3]),
    ([-1, -2, -3, -4, -5], [-1, -1, -1, -1, -1])
]

for i, (nums, expected) in enumerate(test_cases):
    result = stream_max(nums)
    print(f'\nTest {i+1}')
    print(f'Input: {nums}')
    print(f'Expected Output: {expected}')
    print(f'Actual Output: {result}')
    if result == expected:
        print('Status: Passed')
    else:
        print('Status: Failed')