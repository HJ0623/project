class Node:
    def __init__(self, elem, next=None):
        self.data = elem
        self.link = next

class LinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail is None

    def enqueue(self, item):
        node = Node(item, None)
        if self.isEmpty():
            self.tail = node
            node.link = node
        else:
            node.link = self.tail.link
            self.tail.link = node
            self.tail = node

    def dequeue(self):
        if not self.isEmpty():
            data = self.tail.link.data
            if self.tail.link == self.tail:
                self.tail = None
            else:
                self.tail.link = self.tail.link.link
            return data

    def peek(self):
        if not self.isEmpty():
            return self.tail.link.data

def BFS(maze, start, end):
    que = LinkedQueue()
    que.enqueue(start)

    while not que.isEmpty():
        here = que.dequeue()
        x, y = here

        if maze[y][x] == 'x':
            return True

        maze[y][x] = '.'
        
        if isValidPos(x, y - 1):
            que.enqueue((x, y - 1))  # 상
        if isValidPos(x + 1, y):
            que.enqueue((x + 1, y))  # 우
        if isValidPos(x, y + 1):
            que.enqueue((x, y + 1))  # 하
        if isValidPos(x - 1, y):
            que.enqueue((x - 1, y))  # 좌

    return False

def isValidPos(x, y):
    return 0 <= x < MAZE_SIZE and 0 <= y < MAZE_SIZE and (maze[y][x] == '0' or maze[y][x] == 'x')

# Maze 설정
MAZE_SIZE = 11

maze = [
    ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■'],
    ['e', '0', '■', '0', '0', '■', '0', '0', '0', '■', '■'],
    ['■', '0', '■', '■', '0', '0', '0', '■', '0', '■', '■'],
    ['■', '0', '0', '0', '■', '■', '■', '■', '0', '0', '■'],
    ['■', '■', '■', '0', '0', '■', '0', '0', '0', '■', '■'],
    ['■', '0', '■', '0', '■', '■', '0', '■', '■', '0', '■'],
    ['■', '0', '■', '0', '0', '0', '0', '■', '0', '0', '■'],
    ['■', '0', '■', '■', '■', '0', '■', '■', '■', '0', '■'],
    ['■', '0', '0', '0', '■', '0', '0', '0', '0', '0', 'x'],
    ['■', '■', '■', '■', '■', '■', '■', '■', '■', '■', '■']
]

start = (0, 1)
end = (10, 9)

if BFS(maze, start, end):
    print('미로 탐색 성공')
else:
    print('미로 탐색 실패')
