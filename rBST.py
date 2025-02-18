def fact(num):
    if num ==1:
        return 1
    else:
        return num * fact(num-1)
         

#print(fact(10))

class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BST:
    def __init__(self):
        self.root = None

    def __r_contains(self,node,value):
        if node is None:
            return False
        if node.value == value:
            return True
        if value > node.value:
            return self.__r_contains(node.right,value)
        else:
            return self.__r_contains(node.left,value)
        
    ''' 
    def __r_insert(self,node,value):
        if value > node.value:
            if node.right is None:
                node.right = Node(value)
                return True
            return self.__r_insert(node.right,value)
        elif value < node.value:
            if node.left is None:
                node.left = Node(value)
                return True
            return self.__r_insert(node.left,value)
        else:
            return False
    '''
    def __r_insert(self,current_node,value):
        if current_node == None:
            return Node(value)
        if value < current_node.value:
            current_node.left = self.__r_insert(current_node.left,value)
        elif value > current_node.value:
            current_node.right = self.__r_insert(current_node.right,value)
        return current_node

    
    def min_value(self,node):
        if node.left is None:
            return node.value
        else:
            return self.min_value(node.left)


    def __r_delete(self,current_node,value):
        if current_node is None:
            return None
        if value < current_node.value:
            current_node.left = self.__r_delete(current_node.left,value)
        elif value > current_node.value:
            current_node.right = self.__r_delete(current_node.right,value)
        else:
            # when value is equal, node found
            if current_node.left is None and current_node.right is None:
                return None # this is set the parent node left or right to None and detach the node from tree
            elif current_node.left is None:
                #return current_node.right
                current_node = current_node.right
            elif current_node.right is None:
                #return current_node.left
                current_node = current_node.left
            else:
                sub_min_value = self.min_value(current_node.right)
                current_node.value = sub_min_value
                current_node.right = self.__r_delete(current_node.right, sub_min_value)

        return current_node

    def __print_tree(self,node):
        if node is None:
            return 
        else:
            print(node.value)
            self.__print_tree(node.right)
            self.__print_tree(node.left)
    
    def print_tree(self):
        self.__print_tree(self.root)
       

    def insert(self,value):
        n = Node(value)
        if self.root is None:
            self.root = n
            return True
        
        temp_node = self.root
        while True:
            if value > temp_node.value :
                if temp_node.right == None:
                    temp_node.right = n
                    return True
                temp_node = temp_node.right
            else:
                if temp_node.left == None:
                    temp_node.left = n
                    return True
                temp_node = temp_node.left
        
    def __find_min(self,start_node):
        temp = start_node
        while temp.left is not None:
            parent = temp
            temp = temp.left
        return parent

    def r_contains(self,value):
        return self.__r_contains(self.root,value)
    
    def r_insert(self,value):
        if self.root is None:
            self.root = Node(value)
        else:
            self.__r_insert(self.root,value)

    def delete(self,value):
        temp = self.root
        parent = self.root

        while True:
            if temp.value == value:
                if temp.right is None and temp.left is None:
                    if temp.value < parent.value:
                        parent.left = None
                    else:
                        parent.right = None 
                elif temp.right is None and temp.left is not None:
                    if temp.value <parent.value:
                        parent.left = temp.left
                    else:
                        parent.right = temp.left
                elif temp.left is None and temp.right is not None:
                    if temp.value <parent.value:
                        parent.left = temp.right
                    else:
                        parent.right = temp.right
                else:
                    min_node_parent = self.__find_min(temp)
                    temp.value = min_node_parent.left.value
                    temp = min_node_parent.left
                    min_node_parent.left = None

                return temp
            else:
                parent = temp
                if value > temp.value:
                    temp = temp.right
                else:
                    temp = temp.left
                
    def r_delete(self,value):
        self.__r_delete(self.root,value)

    def BFS(self): # breath first search
        queue = []
        results = []
        current_node = self.root
        queue.append(current_node)

        while len(queue)>0:    
            current_node = queue.pop(0)
            results.append(current_node.value)
            if current_node.left is not None:
                queue.append(current_node.left)
            if current_node.right is not None:
                queue.append(current_node.right)
            
        return results

    def dfs_preorder(self):
        results = []
        
        #write a recursive function for traversal.
        def traverse(current_node):
            results.append(current_node.value)

            if current_node.left is not None:
                traverse(current_node.left)
            if current_node.right is not None:
                traverse(current_node.right)

        traverse(self.root)
        return results
    
    def dfs_postorder(self):
        results = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            if current_node.right is not None:
                traversal(current_node.right)
            results.append(current_node.value)

        traversal(self.root)

        return results
    
    def dfs_inorder(self):
        results = []

        def traversal(current_node):
            if current_node.left is not None:
                traversal(current_node.left)
            results.append(current_node.value)
            if current_node.right is not None:
                traversal(current_node.right)

        traversal(self.root)
        return results

    def kth_smallest_value(self,k):

        if self.root is None or k <1:
            return None

        order_list = []

        def traversal(current_node,k):
            
            if current_node.left is not None:
                traversal(current_node.left,k)
                
            order_list.append(current_node.value)

            if len(order_list) >= k:
                return   
            if current_node.right is not None:
                traversal(current_node.right,k)
            
            
                
        traversal(self.root,k)
        print(order_list)
        if k>len(order_list):
            return None
        else:
            return order_list[k-1]
        
    
    def r_kth_smallest(self, k):
        self.kth_smallest_count = 0
        return self.kth_smallest_helper(self.root, k)
 
    def kth_smallest_helper(self, node, k):
        if node is None:
            return None
 
        left_result = self.kth_smallest_helper(node.left, k)
        if left_result is not None:
            return left_result
 
        self.kth_smallest_count += 1
        if self.kth_smallest_count == k:
            return node.value
 
        right_result = self.kth_smallest_helper(node.right, k)
        if right_result is not None:
            return right_result
 
        return None
    
    def kth_smallest(self, k):
        stack = []
        node = self.root
        
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            k -= 1
            if k == 0:
                return node.value
            
            node = node.right
            
        return None




my_bst = BST()
my_bst.r_insert(45)
my_bst.r_insert(40)
my_bst.r_insert(70)
my_bst.r_insert(30)
my_bst.r_insert(42)
my_bst.r_insert(60)
my_bst.r_insert(80)

print(my_bst.kth_smallest_value(2)) # find the 4th smallest element


#print(my_bst.BFS())
#print(my_bst.dfs_preorder())
#print(my_bst.dfs_postorder())
print(my_bst.dfs_inorder())
#print (my_bst.root.value,my_bst.root.right,my_bst.root.left)
