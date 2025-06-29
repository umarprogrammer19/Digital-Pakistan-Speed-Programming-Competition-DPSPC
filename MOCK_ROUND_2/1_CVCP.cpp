#include <iostream>
#include <vector>
#include <climits>
#include <algorithm>
#include <set>

using namespace std;

const int INF = INT_MAX;
void floyd_warshall(int n, vector<vector<int>> &dist)
{
    for (int k = 0; k < n; ++k)
    {
        for (int i = 0; i < n; ++i)
        {
            for (int j = 0; j < n; ++j)
            {
                if (dist[i][k] != INF && dist[k][j] != INF && dist[i][k] + dist[k][j] < dist[i][j])
                {
                    dist[i][j] = dist[i][k] + dist[k][j];
                }
            }
        }
    }
}
bool is_possible(int n, int k, const vector<vector<int>> &dist, int D)
{
    vector<set<int>> cover_sets(n);
    for (int i = 0; i < n; ++i)
    {
        for (int j = 0; j < n; ++j)
        {
            if (dist[i][j] <= D)
            {
                cover_sets[i].insert(j);
            }
        }
    }
    set<int> covered;
    vector<bool> used(n, false);
    for (int _ = 0; _ < k; ++_)
    {
        int best = -1;
        int max_new_covered = -1;
        for (int i = 0; i < n; ++i)
        {
            if (used[i])
            {
                continue;
            }
            int new_covered = 0;
            for (int j : cover_sets[i])
            {
                if (covered.find(j) == covered.end())
                {
                    new_covered++;
                }
            }
            if (new_covered > max_new_covered)
            {
                max_new_covered = new_covered;
                best = i;
            }
        }
        if (best == -1)
        {
            break;
        }
        used[best] = true;
        covered.insert(cover_sets[best].begin(), cover_sets[best].end());
    }
    return covered.size() == n;
}

int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m, k;
    cin >> n >> m >> k;
    vector<vector<int>> dist(n, vector<int>(n, INF));
    for (int i = 0; i < n; ++i)
    {
        dist[i][i] = 0;
    }
    for (int i = 0; i < m; ++i)
    {
        int u, v, w;
        cin >> u >> v >> w;
        u--;
        v--;
        dist[u][v] = min(dist[u][v], w);
        dist[v][u] = min(dist[v][u], w);
    }

    floyd_warshall(n, dist);

    int low = 0, high = 10000 * n;
    int ans = high;
    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (is_possible(n, k, dist, mid))
        {
            ans = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }
    cout << ans << endl;
    return 0;
}