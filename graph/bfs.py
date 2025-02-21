import deque

def bfs(G: dict[int, list[int]], u: int, v: int, n: int) -> bool:
    # checks if path [u -> v] exists
    # G can contain cycles

    seen = [False] * n
    q = deque([u])
    while q:
        u = q.popleft()
        if u == v:
            return True
        if not seen[u]:
            seen[u] = True
            q.extend(G[u])
    return False


def bfs(G: dict[int, list[int]], u: int, v: int) -> list[int]:
    # given DAG
    # return path [u -> v]

    q = deque([[u]])
    while q:
        path = q.popleft()
        u = path[-1]
        if u == v:
            return path
        for v in G[u]:
            q.append(path[:] + [v])
    return []
