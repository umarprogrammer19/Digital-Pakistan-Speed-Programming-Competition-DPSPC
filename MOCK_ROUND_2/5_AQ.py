from collections import deque
import heapq


class Edge:
    def __init__(self, to, rev, cap, original_cap=0):
        self.to = to
        self.rev = rev
        self.cap = cap
        self.original_cap = original_cap


class MaxFlow:
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]

    def add(self, fr, to, cap):
        forward = Edge(to, len(self.graph[to]), cap, cap)
        backward = Edge(fr, len(self.graph[fr]), 0)
        self.graph[fr].append(forward)
        self.graph[to].append(backward)

    def bfs_level(self, s, t, level):
        queue = deque()
        level[s] = 0
        queue.append(s)
        while queue:
            v = queue.popleft()
            for e in self.graph[v]:
                if e.cap > 0 and level[e.to] < 0:
                    level[e.to] = level[v] + 1
                    queue.append(e.to)
        return level[t] != -1

    def dfs_flow(self, level, iter, v, t, upTo):
        if v == t:
            return upTo
        for i in range(iter[v], len(self.graph[v])):
            e = self.graph[v][i]
            if e.cap > 0 and level[v] < level[e.to]:
                d = self.dfs_flow(level, iter, e.to, t, min(upTo, e.cap))
                if d > 0:
                    e.cap -= d
                    self.graph[e.to][e.rev].cap += d
                    return d
            iter[v] += 1
        return 0

    def max_flow(self, s, t):
        flow = 0
        level = [-1] * self.n
        INF = 10**18
        while self.bfs_level(s, t, level):
            iter = [0] * self.n
            f = self.dfs_flow(level, iter, s, t, INF)
            while f > 0:
                flow += f
                f = self.dfs_flow(level, iter, s, t, INF)
            level = [-1] * self.n
        return flow


def solve_adversarial_restoration(T, all_cases):
    results = []

    for test in all_cases:
        N, M, K = test["N"], test["M"], test["K"]
        D, B = test["D"], test["B"]
        lines = test["lines"]

        base_edges = []
        upgrades = []

        for u, v, c, x, p in lines:
            base_edges.append((u, v, c))
            upgrades.append((u, v, c + x, p))

        def is_possible(required_flow):
            # Try all subsets of upgrades within budget to find one that sustains required_flow even after K edge removals
            heap = []
            for i in range(M):
                u, v, cx, p = upgrades[i]
                heapq.heappush(heap, (p, i))  # prioritize cheaper upgrades

            selected = set()
            total_cost = 0
            while heap and total_cost <= B:
                p, idx = heapq.heappop(heap)
                if total_cost + p > B:
                    break
                selected.add(idx)
                total_cost += p

            # Build final upgraded graph
            mf = MaxFlow(N)
            edges_with_capacity = []

            for i in range(M):
                u, v = base_edges[i][0], base_edges[i][1]
                cap = base_edges[i][2]
                if i in selected:
                    cap = upgrades[i][2]
                mf.add(u, v, cap)
                mf.add(v, u, cap)
                edges_with_capacity.append(((u, v), cap))

            maxflow = mf.max_flow(0, N - 1)
            if maxflow < required_flow:
                return False, maxflow

            # Sort edges by capacity (worst sabotage = remove K highest capacity contributing edges)
            edges_sorted = sorted(edges_with_capacity, key=lambda x: -x[1])
            total_cut = 0
            count = 0
            for edge, cap in edges_sorted:
                if count == K:
                    break
                total_cut += cap
                count += 1

            return (maxflow - total_cut) >= required_flow, maxflow - total_cut

        low, high = 0, 10**9
        best_flow = 0
        answer = 0

        while low <= high:
            mid = (low + high) // 2
            possible, flow = is_possible(mid)
            if possible:
                answer = 1
                best_flow = mid
                low = mid + 1
            else:
                high = mid - 1

        results.append((answer, best_flow))

    return results


# Prepare input as expected by function
T = 2
all_cases = [
    {
        "N": 5,
        "M": 3,
        "K": 1,
        "D": 3,
        "B": 3,
        "lines": [(0, 1, 2, 2, 2), (1, 2, 2, 1, 1), (0, 2, 1, 1, 1)],
    },
    {
        "N": 7,
        "M": 5,
        "K": 2,
        "D": 4,
        "B": 5,
        "lines": [
            (0, 1, 3, 2, 2),
            (1, 2, 2, 2, 2),
            (2, 3, 2, 2, 2),
            (0, 2, 1, 2, 1),
            (1, 3, 1, 1, 1),
        ],
    },
]

print(solve_adversarial_restoration(T, all_cases))
