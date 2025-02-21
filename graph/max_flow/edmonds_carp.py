# Pseudocode из Кормена
# G = (V, E)
# G_f = (V, E)
# 
# for edge in G.E:
#     edge.f = 0
# while path := increasing_path_exists(G_f):
#     c_f_p = min(edge.c_f for edge in path)
#     for edge in path:
#         if edge in G.E:
#             edge.f = edge.f + c_f_p
#         else:
#             edge.f = edge.f - c_f_p
import collections

def bfs(
        adj: dict[int, list[tuple[int, int]]], 
        capacity: list[list[int]],
        parent: list[int],
        source: int, 
        sink: int,
) -> list[tuple[int, int]]:
    # Дан DAG
    # Вернем min flow
    parent[source] = -2
    q = collections.deque([(source, float('inf'))])
    while q:
        u, flow = q.popleft()
        for v in adj[u]:
            if parent[v] == -1 and capacity[u][v] > 0:
                parent[v] = u
                new_flow = min(flow, capacity[u][v])
                if v == sink:
                    return new_flow
                q.append((v, new_flow))
    

def max_flow(n: int, edges: list[tuple[int, int, int]], source: int, sink: int) -> int:
    # Дан DAG, вернем макс поток между source и sink
    capacity = [[0] * n for _ in range(n)]
    # Переведем DAG в undirected adj
    adj = collections.defaultdict(list)
    for u, v, c in edges:
        adj[u].append(v)
        adj[v].append(u)
        capacity[u][v] = c
    
    flow = new_flow = 0
    # С помощью вектора будет поддерживать последний путь
    parent = [-1] * n
    while new_flow := bfs(adj, capacity, parent, source, sink):
        flow += new_flow
        
        # Обновим residual network
        cur = sink
        while cur != source:
            prev = parent[cur]
            capacity[prev][cur] -= new_flow
            capacity[cur][prev] += new_flow
            cur = prev
        parent = [-1] * n
    
    return flow

# u -> [(v, capacity)]
edges = [
    (0, 1, 16), (0, 2, 13),
    (1, 3, 12),
    (2, 1, 4), (2, 4, 14),
    (3, 2, 9), (3, 5, 20),
    (4, 3, 7), (4, 5, 4)
]

assert max_flow(6, edges, 0, 5) == 23
