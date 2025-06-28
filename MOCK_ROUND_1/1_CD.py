def count_triangles(n, edges):
    from collections import defaultdict

    graph = defaultdict(set)
    for u, v in edges:
        graph[u].add(v)
        graph[v].add(u)

    count = 0

    for u in range(n):
        for v in graph[u]:
            if v > u:
                for w in graph[v]:
                    if w > v and w in graph[u]:
                        count += 1
    return count


n, m = map(int, input().split())
edges = [tuple(map(int, input().split())) for _ in range(m)]

print(count_triangles(n, edges))
