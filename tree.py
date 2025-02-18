class Node:
    def __init__(self,value):
        self.value = value
        self.right = None
        self.left = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self,value):
        new_node = Node(value)
        print(new_node)
        if self.root is None:
            self.root = new_node
            return True
        temp = self.root
        while (True):
            if new_node.value > temp.value:
                if temp.right is None:
                    temp.right = new_node
                    return True
                temp = temp.right
            elif new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                temp = temp.left
            else:
                return False

    def contains(self,value):
        temp = self.root

        while temp:
            if temp.value == value:
                return True
            else:
                if value > temp.value:
                    temp = temp.right
                elif value < temp. value:
                    temp = temp.left

        return False


       
bst = BinarySearchTree()
bst.insert(10)
bst.insert(5)
bst.insert(15)
result = bst.insert(3)
print(result, bst.root.left.left.left)