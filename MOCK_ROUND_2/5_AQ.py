from collections import deque
from itertools import combinations
import sys

sys.setrecursionlimit(10000)


def bfs(capacity, flow, s, t, parent):
    visited = set()
    queue = deque([s])
    visited.add(s)
    while queue:
        u = queue.popleft()
        for v in range(len(capacity)):
            if v not in visited and capacity[u][v] - flow[u][v] > 0:
                parent[v] = u
                visited.add(v)
                if v == t:
                    return True
                queue.append(v)
    return False


def edmonds_karp(n, capacity, s, t):
    flow = [[0] * n for _ in range(n)]
    total_flow = 0
    parent = [-1] * n
    while bfs(capacity, flow, s, t, parent):
        path_flow = float("inf")
        v = t
        while v != s:
            u = parent[v]
            path_flow = min(path_flow, capacity[u][v] - flow[u][v])
            v = u
        v = t
        while v != s:
            u = parent[v]
            flow[u][v] += path_flow
            flow[v][u] -= path_flow
            v = u
        total_flow += path_flow
    return total_flow


def solve_case(N, M, K, D, B, edges):
    from itertools import combinations

    # Try all combinations of upgrades within budget
    upgrade_combinations = []

    # Generate all subsets of upgrades (naive brute-force)
    for mask in range(1 << M):
        cost = 0
        updated_edges = []
        for i in range(M):
            u, v, c, x, p = edges[i]
            cap = c
            if (mask >> i) & 1:
                if cost + p > B:
                    break
                cap += x
                cost += p
            updated_edges.append((u, v, cap, i))  # i is edge index
        else:
            upgrade_combinations.append((updated_edges, cost))

    best_result = (0, 0)

    for edge_list, total_cost in upgrade_combinations:
        base_edges = edge_list[:]
        # Try all combinations of K edges to destroy
        worst_flow = float("inf")
        indices = [e[3] for e in base_edges]  # all edge indices
        for removed in combinations(range(len(base_edges)), K):
            # Build capacity matrix
            capacity = [[0] * N for _ in range(N)]
            for idx, (u, v, cap, i) in enumerate(base_edges):
                if idx in removed:
                    continue
                capacity[u][v] += cap  # directed edge
            f = edmonds_karp(N, capacity, 0, N - 1)
            worst_flow = min(worst_flow, f)
            if worst_flow < D:
                break  # no need to continue
        if worst_flow >= D:
            best_result = (1, worst_flow)
            break
        else:
            best_result = max(best_result, (0, worst_flow), key=lambda x: x[1])

    return best_result


# MAIN
T = int(input())
for _ in range(T):
    N, M, K = map(int, input().split())
    D, B = map(int, input().split())
    edges = []
    for _ in range(M):
        u, v, c, x, p = map(int, input().split())
        edges.append((u, v, c, x, p))
    res, flow = solve_case(N, M, K, D, B, edges)
    print(f"{res} {flow}")
