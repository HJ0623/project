
class ArrayStack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.array = [None] * capacity
        self.top = -1
        
    def isEmpty(self):
        return self.top == -1
    
    def isFull(self):
        return self.top == self.capacity - 1
    
    def push(self, data):
        if self.isFull():
            print("Stack is full!")
            pass
        else:
            self.top += 1
            self.array[self.top] = data
            
    def pop(self):
        if self.isEmpty():
            print("Stack is empty!")
            pass
        else:
            data = self.array[self.top]
            self.top -= 1
            return data
        
    def peek(self):
        if self.isEmpty():
            print("Stack is empty!")
            pass
        else:
            return self.array[self.top]

class CircularQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.front = 0
        self.rear = 0
        
        
    def isEmpty(self):
        return self.front == self.rear
    
    def isFull(self):
        return self.front == (self.rear + 1) % self.capacity
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear + 1) % self.capacity
            self.array[self.rear] = item
        else:
            pass
    
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front + 1) % self.capacity
            return self.array[self.front]
        else: 
            pass
    
    def peek(self):
        if not self.isEmpty():
            return self.array[(self.front + 1) % self.capacity]
        else:
            pass
        
class PriorityQueue:
    def __init__(self, capacity = 10):
        self.capacity = capacity
        self.array = [None] * capacity
        self.size = 0
        
    def isEmpty(self):
        return self.size == 0
    
    def isFull(self):
        return self.size == self.capacity
    
    def enqueue(self, item):
        if not self.isFull():
            self.array[self.size] = item
            self.size += 1
        else:
            print("Queue is full!")
            pass
    
    def findMaxIndex(self):
        if self.isEmpty():
            return -1
        
        highest = 0
        for i in range(1, self.size):
            if self.array[i][2] > self.array[highest][2]:
                highest = i
        
        return highest
    
    def dequeue(self):
        highest = self.findMaxIndex()
        
        if highest != -1:
            self.size -= 1
            self.array[highest], self.array[self.size] = self.array[self.size], self.array[highest]
            return self.array[self.size]

    def peek(self):
        highest = self.findMaxIndex()
        if highest != -1:
            return self.array[highest]

    def __str__(self):
        return str(self.array[0:self.size])