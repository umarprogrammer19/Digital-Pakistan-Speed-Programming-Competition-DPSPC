from collections import defaultdict, deque


def min_hops(n, routes, source, destination):
    stop_to_routes = defaultdict(set)

    for i, route in enumerate(routes):
        for stop in route:
            stop_to_routes[stop].add(i)

    if source == destination:
        return 0

    graph = defaultdict(set)
    for stop, route_set in stop_to_routes.items():
        route_list = list(route_set)
        for i in range(len(route_list)):
            for j in range(i + 1, len(route_list)):
                a, b = route_list[i], route_list[j]
                graph[a].add(b)
                graph[b].add(a)

    source_routes = stop_to_routes.get(source, set())
    dest_routes = stop_to_routes.get(destination, set())

    if not source_routes or not dest_routes:
        return -1

    visited = set()
    queue = deque()

    for r in source_routes:
        queue.append((r, 1))  
        visited.add(r)

    while queue:
        current_route, hops = queue.popleft()
        if current_route in dest_routes:
            return hops

        for neighbor in graph[current_route]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, hops + 1))

    return -1 

n = int(input())
routes = []
for _ in range(n):
    route = list(map(int, input().split()))
    routes.append(route)

source, destination = map(int, input().split())
print(min_hops(n, routes, source, destination))
