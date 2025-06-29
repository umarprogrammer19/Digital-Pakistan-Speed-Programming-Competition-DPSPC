from collections import defaultdict


def min_vertex_cover(n, edges):
    # Build adjacency list
    graph = defaultdict(list)
    for u, v in edges:
        graph[u - 1].append(v - 1)
        graph[v - 1].append(u - 1)

    # dp[node][0] = min vertex cover excluding node, dp[node][1] = including node
    dp = [[float("inf"), float("inf")] for _ in range(n)]
    visited = [False] * n

    def dfs(node, parent):
        visited[node] = True
        # Leaf node case
        if len(graph[node]) == 1 and node != 0:  # Leaf (not root)
            dp[node][0] = 0  # Don't include leaf
            dp[node][1] = 1  # Include leaf
            return

        # Initialize for node included
        dp[node][1] = 1  # Count the node itself
        exclude_sum = 0
        # Process children
        for child in graph[node]:
            if child != parent:
                dfs(child, node)
                # If node included, take min of child included/excluded
                dp[node][1] += min(dp[child][0], dp[child][1])
                # If node excluded, must include all children
                exclude_sum += dp[child][1]

        # Set exclude case (all children must be included)
        dp[node][0] = exclude_sum

    # Start DFS from root (node 0)
    dfs(0, -1)

    # Return minimum vertex cover size
    return min(dp[0][0], dp[0][1])


# Read input
n = int(input())
edges = []
for _ in range(n - 1):
    u, v = map(int, input().split())
    edges.append((u, v))

# Output result
print(min_vertex_cover(n, edges))
