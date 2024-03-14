def DFS_AL(vtx, aList, s, visited):
   if 0 <= s < len(vtx):
        print(vtx[s], end=' ')
        visited[s] = True
        for v in aList[s]:
            if 0 <= v < len(vtx) and not visited[v]:
                DFS_AL(vtx, aList, v, visited)

vertex = ['1', '2', '3', '4', '5', '6', '7', '8']
adjList = [
    [2, 3, 7],
    [1, 3, 6],
    [1, 2, 6, 7],
    [5, 7],
    [4, 6],
    [2, 3, 5],
    [1, 3, 4, 8],
    [7]
]
print('DFS_AL(시작:A): ', end="")
DFS_AL(vertex, adjList, 0, [False] * len(vertex))
print()