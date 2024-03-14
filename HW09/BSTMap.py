from BinSrchTree import *

def inorder(n) :
    if n is not None :
        inorder(n.left)
        print(n.key, end=' ')   # node의 key만 중위순회로 출력
        inorder(n.right)

# 코드 9.11: 이진탐색트리를 이용한 맵 클래스
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


if __name__ == "__main__":
    new_data = [50, 25, 75, 15, 35, 60, 90, 10, 40, 70]
    new_values = ["오십", "이오", "칠오", "십오", "삼십오", "육십", "구십", "십", "사십", "칠십"]

    map = BSTMap()
    map.display("[Initial] : ")

    for i in range(len(new_data)):
        map.insert(new_data[i], new_values[i])
        map.display("[Insert %2d] : " % new_data[i])

   
    print('[Max Key] : ', map.findMax().key)
    print('[Min Key] : ', map.findMin().key)

   
    print('[Search 25] : ', 'Success' if map.search(25) is not None else 'Failure')
    print('[Search 55] : ', 'Success' if map.search(55) is not None else 'Failure')
    print('[Search 칠오] : ', 'Success' if map.searchValue("칠오") is not None else 'Failure')
    print('[Search 이오] : ', 'Success' if map.searchValue("이오") is not None else 'Failure')

    map.delete(15)
    map.display("[Delete 15] : ")
    map.delete(75)
    map.display("[Delete 75] : ")
    map.delete(50)
    map.display("[Delete 50] : ")
    map.delete(35)
    map.display("[Delete 35] : ")
