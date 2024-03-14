import copy
import sys
import time
import os

class Node:
    def __init__ (self, elem, next=None):
        self.data = elem
        self.link = next

class LinkedQueue:
    def __init__(self):
        self.tail = None

    def isEmpty(self):
        return self.tail == None

    def isFull(self):
        return False

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

    def size(self):
        if self.isEmpty():
            return 0
        else:
            count = 1
            node = self.tail.link
            while not node == self.tail:
                node = node.link
                count += 1
            return count

    def __str__(self):
        arr = []
        if not self.isEmpty():
            node = self.tail.link
            while not node == self.tail:
                arr.append(node.data)
                node = node.link
            arr.append(node.data)
        return str(arr)

def drawMaze(maze, current_x, current_y):
    os.system('cls' if os.name == 'nt' else 'clear')
    w = len(maze[0])
    h = len(maze)
    for i in range(h):
        for j in range(w):
            if (j, i) == (current_x, current_y):
                print("★", end=" ")
            else:
                print(maze[i][j], end=" ")
        print()
    time.sleep(0.5)

def isValidPos(x, y, maze):
    if 0 <= x < len(maze[0]) and 0 <= y < len(maze):
        if maze[y][x] == '0' or maze[y][x] == 'x':
            return True
    return False

def BFS(maze, start, end):
    que = LinkedQueue()
    que.enqueue(start)
    print('BFS: ')

    while not que.isEmpty():
        here = que.dequeue()
        x, y = here

        if maze[y][x] == 'x':
            return True

        maze[y][x] = '.'
        drawMaze(maze, x, y)

        if isValidPos(x, y - 1, maze):
            que.enqueue((x, y - 1))  # 상
        if isValidPos(x + 1, y, maze):
            que.enqueue((x + 1, y))  # 우
        if isValidPos(x, y + 1, maze):
            que.enqueue((x, y + 1))  # 하
        if isValidPos(x - 1, y, maze):
            que.enqueue((x - 1, y))  # 좌

    return False

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

MAZE_SIZE = 11

result = None
current_x = 0
current_y = 1

if __name__ == "__main__":
    while True:
        drawMaze(maze, current_x, current_y)
        print("1. BFS\n2. Quit")
        choice = input("Choose an option: ")

        result = None
        current_x, current_y = 0, 1

        if choice == '1':
            print("\nBFS result:")
            org = copy.deepcopy(maze)
            result = BFS(maze, (current_x, current_y), (10, 9))
        elif choice == '2':
            break
        else:
            print("Invalid option. Please choose 1 (BFS) or 2 (Quit).")

        if result:
            print('--> Maze solved!')
        else:
            print('--> Maze not solved.')
