import sys
sys.setrecursionlimit(10**7)
def dfs(u, p, adj, dp):
    a = 1  
    b = 0 
    for v in adj[u]:
        if v == p:
            continue
        dfs(v, u, adj, dp)
        a += dp[v][0]
        b += max(dp[v][0], dp[v][1])
    dp[u][0] = b
    dp[u][1] = a
def main():
    n = int(sys.stdin.readline())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().split())
        adj[x].append(y)
        adj[y].append(x)
    dp = [[0, 0] for _ in range(n + 1)]
    dfs(1, -1, adj, dp)
    res = max(dp[1][0], dp[1][1])
    print(0 if res == 1 else 1)
main()
