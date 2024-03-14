from queue import Queue

def BFS_AM(vtx, aMat, s):
    n = len(vtx)
    visited = [False] * n
    Q = Queue()
    Q.put(s)
    visited[s] = True
    while not Q.empty():
        s = Q.get()
        print(vtx[s], end=' ')
        for v in range(n):
            if aMat[s][v] != 0 and not visited[v]:
                Q.put(v)
                visited[v] = True

vertex = ['1', '2', '3', '4', '5', '6','7', '8']
adjMat = [
    [0, 1, 1, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 0],
    [1, 1, 0, 0, 0, 1, 1, 0],
    [0, 0, 0, 0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0, 1, 0, 0],
    [0, 1, 1, 0, 1, 0, 0, 0],
    [1, 0, 1, 1, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 0, 1, 0]
]
print('BFS_AM(시작:A): ', end="")
BFS_AM(vertex, adjMat, 0)
print()