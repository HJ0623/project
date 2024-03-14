# 코드 11.11: dist가 최소인 정점 탐색 함수 
INF = 9999
def getMinVertex(dist, selected) :
    minv = 0
    mindist = INF
    for v in range(len(dist)) :
        if selected[v] ==False and dist[v]<mindist :
            mindist = dist[v]
            minv = v
    return minv

# 코드 11.12: Prim의 MST 알고리즘
def MSTPrim(vertex, adj) :
    vsize = len(vertex)
    dist = [INF] * vsize
    selected = [False] * vsize
    dist[0] = 0
    totalWeight = 0  # MST의 가중치 합 초기화

    for i in range(vsize) :
        u = getMinVertex(dist, selected)
        selected[u] = True;
        totalWeight += dist[u]  # 선택된 정점의 가중치를 MST의 총 가중치에 더함
        print(vertex[u], end=' ')

        for v in range(vsize) :
            if (adj[u][v] != None) :
                if not selected[v] and adj[u][v]< dist[v] :
                    dist[v] = adj[u][v]
    print()
    print("MST의 총 가중치:", totalWeight)

if __name__ == "__main__":
    vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    weights = [
        [None, 25, 5, None, None, None, 48, None],
        [25, None, 3, None, None, 7, None, None],
        [5, 3, None, None, None, 6, 4, None],
        [None, None, None, None, 11, None, 19, None],
        [None, None, None, 11, None, 20, None, None],
        [None, 7, 6, None, 20, None, None, None],
        [48, None, 4, 19, None, None, None, 37],
        [None, None, None, None, None, None, 37, None]
    ]

    print("Prim 알고리즘 ")
    MSTPrim(vertex, weights)