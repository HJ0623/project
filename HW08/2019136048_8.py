# CircularQueue.py
class CircularQueue :
    def __init__( self, capacity = 8 ) :
        self.capacity = capacity        # 용량(고정)
        self.array = [None] * capacity  # 요소들을 저장할 배열
        self.front = 0                  # 전단의 인덱스
        self.rear = 0                   # 후단의 인덱스

    def isEmpty( self ) :
       return self.front == self.rear

    def isFull( self ) :
       return self.front == (self.rear+1)%self.capacity

    def enqueue( self, item ):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item

    def dequeue( self ):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]

    def peek( self ):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]

    def size( self ) :
       return (self.rear - self.front + self.capacity) % self.capacity

    def __str__(self):
        if self.front < self.rear :
            return str(self.array[self.front+1:self.rear+1])
        else :
            return str(self.array[self.front+1:self.capacity] + \
                       self.array[0:self.rear+1] )


class TNode:
    def __init__ (self, elem, left, right):
        self.data = elem 
        self.left = left
        self.right = right

    def isLeaf(self):
        return self.left is None and self.right is None

def levelorder(root) :
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty() :
        n = queue.dequeue()
        if n is not None :
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

# 코드 8.6: 이진트리의 노드 수 계산
def count_node(n) :
    if n is None : 
        return 0
    else : 
        return 1 + count_node(n.left) + count_node(n.right)

# 코드 8.7: 이진트리의 단말노드 수 계산      
def count_leaf(n) :
    if n is None : return 0
    elif n.isLeaf() : return 1
    else : return count_leaf(n.left) + count_leaf(n.right)


# 코드 8.8: 이진트리의 트리의 높이 계산
def calc_height(n) :
    if n is None : return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight) : return hLeft + 1
    else: return hRight + 1

def is_complete_binary_tree(root):
    
    if root is None:
        return True

    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        node = queue.dequeue()

        if node:
            queue.enqueue(node.left)
            queue.enqueue(node.right)
        else:
            # If a None node is encountered, all the remaining nodes in the queue should also be None.
            while not queue.isEmpty():
                next_node = queue.dequeue()
                if next_node:
                    return False

    return True

def level(root, node):
    if root is None:
        return 0

    queue = CircularQueue()
    queue.enqueue((root, 1)) 

    while not queue.isEmpty():
        current_node, current_level = queue.dequeue()

        if current_node.data == node:
            return current_level

        if current_node.left:
            queue.enqueue((current_node.left, current_level + 1))
        if current_node.right:
            queue.enqueue((current_node.right, current_level + 1))

    return 0

def is_balanced(root):
    def check_balance(node):
        if node is None:
            return True, 0

        left_balanced, left_height = check_balance(node.left)
        right_balanced, right_height = check_balance(node.right)

        height = max(left_height, right_height) + 1
        is_subtree_balanced = abs(left_height - right_height) <= 1

        return left_balanced and right_balanced and is_subtree_balanced, height

    balanced, _ = check_balance(root)
    return balanced

if __name__ == "__main__":
    c = TNode('C', None, None)
    d = TNode('D', None, None)
    b = TNode('B', c, d)
    f = TNode('F', None, None)
    e = TNode('E', None, f)
    root = TNode('A', b, e)

    print('\nLevel-Order : ', end='')
    levelorder(root)
    print()

    is_complete = is_complete_binary_tree(root)
    if is_complete:
        print("완전 이진 트리 입니다.")
    else:
        print("완전 이진 트리가 아닙니다.")

    # Find the level of a random node (e.g., 'D')
    target_node = 'B'
    level = level(root, target_node)

    if level != 0:
        print(f"{target_node}의 노드레벨은 {level}")
    else:
        print(f"노드 '{target_node}'는 트리에 없습니다.")


    is_tree_balanced = is_balanced(root)
    if is_tree_balanced:
        print("균형잡힌 트리입니다.")
    else:
        print("균형이 잡히지 않은 트리입니다.")
    
