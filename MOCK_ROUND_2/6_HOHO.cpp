#include <iostream>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <queue>
#include <set>

using namespace std;
int min_hops(int n, const vector<vector<int>> &routes, int source, int destination)
{
    unordered_map<int, unordered_set<int>> stop_to_routes;
    for (int i = 0; i < n; ++i)
    {
        for (int stop : routes[i])
        {
            stop_to_routes[stop].insert(i);
        }
    }
    if (source == destination)
        return 0;

    unordered_map<int, unordered_set<int>> graph;

    for (const auto &[stop, route_set] : stop_to_routes)
    {
        vector<int> route_list(route_set.begin(), route_set.end());
        for (size_t i = 0; i < route_list.size(); ++i)
        {
            for (size_t j = i + 1; j < route_list.size(); ++j)
            {
                int a = route_list[i], b = route_list[j];
                graph[a].insert(b);
                graph[b].insert(a);
            }
        }
    }

    unordered_set<int> source_routes = stop_to_routes[source];
    unordered_set<int> dest_routes = stop_to_routes[destination];

    if (source_routes.empty() || dest_routes.empty())
        return -1;

    unordered_set<int> visited;
    queue<pair<int, int>> q;

    for (int r : source_routes)
    {
        q.emplace(r, 1);
        visited.insert(r);
    }

    while (!q.empty())
    {
        auto [current_route, hops] = q.front();
        q.pop();

        if (dest_routes.count(current_route))
        {
            return hops;
        }

        for (int neighbor : graph[current_route])
        {
            if (!visited.count(neighbor))
            {
                visited.insert(neighbor);
                q.emplace(neighbor, hops + 1);
            }
        }
    }

    return -1;
}

int main()
{
    int n;
    cin >> n;

    vector<vector<int>> routes(n);
    for (int i = 0; i < n; ++i)
    {
        int stop;
        while (cin.peek() != '\n' && cin >> stop)
        {
            routes[i].push_back(stop);
        }
        cin.ignore();
    }
    int source, destination;
    cin >> source >> destination;

    cout << min_hops(n, routes, source, destination) << endl;
    return 0;
}
