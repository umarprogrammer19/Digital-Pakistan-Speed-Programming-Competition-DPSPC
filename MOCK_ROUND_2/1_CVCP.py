import sys
import heapq

INF = int(1e9)
def floyd_warshall(n, dist):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

def is_possible(n, k, dist, D):
    cover_sets = []
    for i in range(n):
        reachable = set()
        for j in range(n):
            if dist[i][j] <= D:
                reachable.add(j)
        cover_sets.append(reachable)

    covered = set()
    used = [False] * n
    for _ in range(k):
        best = -1
        max_new_covered = -1
        for i in range(n):
            if used[i]:
                continue
            new_covered = len(cover_sets[i] - covered)
            if new_covered > max_new_covered:
                max_new_covered = new_covered
                best = i
        if best == -1:
            break
        used[best] = True
        covered |= cover_sets[best]

    return len(covered) == n

def CVCP():
    n, m, k = map(int, input().split())
    dist = [[INF] * n for _ in range(n)]
    for i in range(n):
        dist[i][i] = 0
    for _ in range(m):
        u, v, w = map(int, input().split())
        dist[u][v] = min(dist[u][v], w)
        dist[v][u] = min(dist[v][u], w)

    floyd_warshall(n, dist)
    low, high = 0, 10000 * n
    answer = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(n, k, dist, mid):
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    print(answer)
CVCP()
