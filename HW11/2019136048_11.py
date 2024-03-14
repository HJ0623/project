import networkx as nx
import matplotlib.pyplot as plt

# 인접행렬
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

# 가중치
weights = [
    [0, 25, 5, 0, 0, 0, 48, 0],
    [25, 0, 3, 0, 0, 7, 0, 0],
    [5, 3, 0, 0, 0, 6, 4, 0],
    [0, 0, 0, 0, 11, 0, 19, 0],
    [0, 0, 0, 11, 0, 20, 0, 0],
    [0, 7, 6, 0, 20, 0, 0, 0],
    [48, 0, 4, 19, 0, 0, 0, 37],
    [0, 0, 0, 0, 0, 0, 37, 0]
]

# 인접행렬과 가중치를 사용하여 그래프 생성
G = nx.Graph()
for i in range(len(adjMat)):
    for j in range(i + 1, len(adjMat[i])):
        if adjMat[i][j] != 0:
            G.add_edge(i + 1, j + 1, weight=weights[i][j])

# 그래프 시각화
pos = nx.spring_layout(G)  # 레이아웃 정의
labels = nx.get_edge_attributes(G, 'weight')  # 엣지 가중치 레이블
nx.draw(G, pos, with_labels=True, font_weight='bold')  # 그래프 그리기
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)  # 엣지 가중치 레이블 그리기

plt.show()
