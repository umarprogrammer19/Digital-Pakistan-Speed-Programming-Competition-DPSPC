import sys

sys.setrecursionlimit(10**6)
def solve():
    n = int(input())
    tree = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input().split())
        tree[u].append(v)
        tree[v].append(u)
    color = [-1] * (n + 1)
    count = [0, 0]
    def dfs(node, c):
        color[node] = c
        count[c] += 1
        for neighbor in tree[node]:
            if color[neighbor] == -1:
                dfs(neighbor, 1 - c)
    dfs(1, 0)
    print(min(count))  
solve()
