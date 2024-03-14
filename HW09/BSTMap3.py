from BinSrchTree import *

def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.key, end=' ')  
        inorder(n.right)

class BSTMap():
    def __init__ (self):
        self.root = None

    def isEmpty (self):
       return self.root == None

    def findMax(self):
       return search_max_bst(self.root)

    def findMin(self):
       return search_min_bst(self.root)

    def search(self, key):
       return search_bst(self.root, key)
       #return search_bst_iter(self.root, key)

    def searchValue(self, key):
       return search_value_bst(self.root, key)

    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty() :
           self.root = n
        else :
           insert_bst(self.root, n)

    def delete(self, key):
        self.root = delete_bst (self.root, key)

    def findMaxCircular(self):
        if self.root is not None:
            return search_max_bst_circular(self.root)
    
    def findMinCircular(self):
        if self.root is not None:
            return search_min_bst_circular(self.root)

    def insertIter(self, key, value=None):
        new_node = BSTNode(key, value)
        if self.isEmpty():
            self.root = new_node
            return

        current = self.root
        parent = None

        while current is not None:
            parent = current
            if key < current.key:
                current = current.left
            elif key > current.key:
                current = current.right
            else:
                current.value = value
                return

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node


    def display(self, msg = 'BTSMap :'):
        print(msg, end='')
        inorder(self.root)
        print()

class PriorityQueue:
    def __init__(self):
        self.bst_map = BSTMap()

    def insert(self, priority, value):
        self.bst_map.insertIter(priority, value)

    def delete(self):
        max_node = self.bst_map.findMaxCircular()
        if max_node:
            self.bst_map.delete(max_node.key)
            return max_node.value
        else:
            return None

    def peek(self):
        max_node = self.bst_map.findMaxCircular()
        return max_node.value if max_node else None

    def display(self):
        self.bst_map.display("Priority Queue: ")

if __name__ == "__main__":

    priority_queue = PriorityQueue()

    priority_queue.insert(3, "Task 1")
    priority_queue.insert(1, "Task 2")
    priority_queue.insert(2, "Task 3")
    priority_queue.insert(5, "Task 4")

    priority_queue.display()

    peeked_task = priority_queue.peek()
    print("Peeked Task:", peeked_task)

    deleted_task = priority_queue.delete()
    print("Deleted Task:", deleted_task)

    priority_queue.display()
