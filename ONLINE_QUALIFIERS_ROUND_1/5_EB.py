import sys

sys.setrecursionlimit(10**6)


def solve():
    t = int(input())
    for _ in range(t):
        n, q, root = map(int, input().split())
        LOG = 20

        tree = [[] for _ in range(n + 1)]
        up = [[-1] * LOG for _ in range(n + 1)]
        parent = [-1] * (n + 1)

        for _ in range(n - 1):
            u, v = map(int, input().split())
            tree[u].append(v)
            parent[v] = u

        def dfs(u, p):
            up[u][0] = p
            for i in range(1, LOG):
                if up[u][i - 1] != -1:
                    up[u][i] = up[up[u][i - 1]][i - 1]
            for v in tree[u]:
                if v != p:
                    dfs(v, u)

        dfs(root, -1)

        def get_kth_ancestor(u, k):
            for i in range(LOG):
                if u == -1:
                    return -1
                if k & (1 << i):
                    u = up[u][i]
            return u if u != -1 else -1

        for _ in range(q):
            u, k = map(int, input().split())
            print(get_kth_ancestor(u, k))
