
# 코드 11.13: 최단 정점 선택 함수
INF = 999
def choose_vertex(dist, found) :
    min = INF
    minpos = -1

    for i in range(len(dist)) :
        if dist[i]< min and found[i]==False :
            min = dist[i]
            minpos = i
    return minpos;

# 코드 11.14: Dijkstra 알고리즘
def shortest_path_dijkstra(vertex, adj, start) :
    vsize = len(vertex)
    dist = list(adj[start])
    path = [start] * vsize
    found= [False] * vsize

    found[start] = True;
    dist[start] = 0;

    for i in range(vsize) :
        print("Step%2d: "%(i+1), dist)  # 단계별 dist[] 출력용 
        u = choose_vertex(dist, found)
        found[u] = True

        for w in range(vsize) :
            if not found[w] :
                if (dist[u] + adj[u][w] < dist[w]) :
                    dist[w] = dist[u] + adj[u][w];
                    path[w] = u;

    return path


# 코드 11.15: Dijkstra 알고리즘 테스트 프로그램         
if __name__ == "__main__":
    # Shortest Path를 위한 Weighted Graph
    vertex =   ['A',    'B',    'C',    'D',    'E',    'F',    'G' ]
     
    weight = [
        [0, 25, 5, INF, INF, INF, 48, INF],
        [25, 0, 3, INF, INF, 7, INF, INF],
        [5, 3, 0, INF, INF, 6, 4, INF],
        [INF, INF, INF, 0, 11, INF, 19, INF],
        [INF, INF, INF, 11, 0, 20, INF, INF],
        [INF, 7, 6, INF, 20, 0, INF, INF],
        [48, INF, 4, 19, INF, INF, 0, 37],
        [INF, INF, INF, INF, INF, INF, 37, 0]
    ]

    print("최단경로 Dijkstra Algorithm")
    start = 0
    path = shortest_path_dijkstra(vertex, weight, start)

    for end in range(len(vertex)) :
        if end != start :
            print("[최단경로: %s->%s] %s" %(vertex[start], vertex[end], vertex[end]), end='')
            while (path[end] != start) :
                print(" <- %s" % vertex[path[end]], end='')
                end = path[end]
            print(" <- %s" % vertex[path[end]])


