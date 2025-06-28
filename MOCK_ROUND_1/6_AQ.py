import sys
input = sys.stdin.readline

def solve():
    t = int(input())
    for _ in range(t):
        n, q, r = map(int, input().split())
        LOG = 20

        parent = [-1] * (n + 1)
        up = [[-1] * LOG for _ in range(n + 1)]

        # Build parent map and immediate ancestors
        for _ in range(n - 1):
            p, c = map(int, input().split())
            parent[c] = p
            up[c][0] = p

        up[r][0] = -1  # root has no parent

        # Build binary lifting table
        for j in range(1, LOG):
            for i in range(1, n + 1):
                prev = up[i][j - 1]
                if prev != -1:
                    up[i][j] = up[prev][j - 1]

        # Process queries
        for _ in range(q):
            u, k = map(int, input().split())
            for i in range(LOG):
                if k & (1 << i):
                    u = up[u][i]
                    if u == -1:
                        break
            print(u if u != -1 else -1)

solve()
