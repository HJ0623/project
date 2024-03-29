parent = []     # 각 노드의 부모노드 인덱스    
set_size = 0    # 전체 집합의 개수    

# 코드 11.7: Union-Find의 초기화 함수
def init_set(nSets):
    global set_size, parent 
    set_size = nSets;
    parent = []  # 빈 리스트로 초기화
    for i in range(nSets):
        parent.append(-1)        # 맨 처음에는 모든 정점이 각각 고유의 집합    

# 코드 11.8: Union-Find의 find()함수
def find(id):
    while (parent[id] >= 0):
        id = parent[id];
    return id;

# 코드 11.9: Union-Find의 union()함수
def union(s1, s2):
    global set_size
    parent[s1] = s2;
    set_size = set_size - 1;

# 코드 11.1: Kruskal의 MST 알고리즘 (최대 비용 신장 트리 버전)
def MSTKruskalMax(vertex, adj):
    vsize = len(vertex)             # 정점의 개수
    init_set(vsize)                 # 정점 집합 초기화
    eList = []                      # 간선 리스트
    totalWeight = 0                 # MST의 가중치 합 초기화

    for i in range(vsize-1):        # 모든 간선을 리스트에 넣음
        for j in range(i+1, vsize):
            if adj[i][j] is not None:
                eList.append((i, j, adj[i][j]))   # 튜플로 저장

    # 간선 리스트를 가중치의 내림차순으로 정렬
    eList.sort(key=lambda e: e[2], reverse=True)

    edgeAccepted = 0
    while edgeAccepted < vsize - 1:  # 정점 수 - 1개의 간선
        e = eList.pop(0)       # 가장 큰 가중치를 가진 간선 (내림차순으로 정렬했으므로 pop(0))
        uset = find(e[0]);      # 두 정점이 속한 집합 번호
        vset = find(e[1]);

        if uset != vset:        # 두 정점이 다른 집합의 원소이면
            print("간선 추가 : (%s, %s, %d)" %
                  (vertex[e[0]], vertex[e[1]], e[2]))
            union(uset, vset)   # 두 집합을 합함
            totalWeight += e[2]  # 간선의 가중치를 MST의 총 가중치에 더함
            edgeAccepted += 1   # 간선이 하나 추가됨

    print("Max MST의 총 가중치:", totalWeight)

if __name__ == "__main__":

    # 테스트
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

    MSTKruskalMax(vertex, weights)
