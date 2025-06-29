#include <iostream>
#include <vector>
#include <set>
#include <algorithm>

using namespace std;
const int MAX_COST = 1e9;

void computeAllPairsShortestPath(int nodes, vector<vector<int>> &costMatrix)
{
    for (int mid = 0; mid < nodes; ++mid)
    {
        for (int src = 0; src < nodes; ++src)
        {
            for (int dest = 0; dest < nodes; ++dest)
            {
                if (costMatrix[src][mid] + costMatrix[mid][dest] < costMatrix[src][dest])
                {
                    costMatrix[src][dest] = costMatrix[src][mid] + costMatrix[mid][dest];
                }
            }
        }
    }
}
bool canPlaceCenters(int cities, int centers, const vector<vector<int>> &costMatrix, int maxRange)
{
    vector<set<int>> reachable(cities);
    for (int from = 0; from < cities; ++from)
    {
        for (int to = 0; to < cities; ++to)
        {
            if (costMatrix[from][to] <= maxRange)
            {
                reachable[from].insert(to);
            }
        }
    }

    set<int> vaccinated;
    vector<bool> centerUsed(cities, false);

    for (int i = 0; i < centers; ++i)
    {
        int optimalCity = -1;
        int maxCover = -1;

        for (int j = 0; j < cities; ++j)
        {
            if (centerUsed[j])
                continue;

            int newCoverage = 0;
            for (int town : reachable[j])
            {
                if (!vaccinated.count(town))
                {
                    ++newCoverage;
                }
            }

            if (newCoverage > maxCover)
            {
                maxCover = newCoverage;
                optimalCity = j;
            }
        }

        if (optimalCity == -1)
            break;

        centerUsed[optimalCity] = true;
        for (int town : reachable[optimalCity])
        {
            vaccinated.insert(town);
        }
    }

    return vaccinated.size() == cities;
}

void solveVaccinationProblem()
{
    int cityCount, roadCount, vaccineCenters;
    cin >> cityCount >> roadCount >> vaccineCenters;

    vector<vector<int>> cost(cityCount, vector<int>(cityCount, MAX_COST));

    for (int i = 0; i < cityCount; ++i)
    {
        cost[i][i] = 0;
    }

    for (int i = 0; i < roadCount; ++i)
    {
        int u, v, c;
        cin >> u >> v >> c;
        cost[u][v] = min(cost[u][v], c);
        cost[v][u] = min(cost[v][u], c);
    }

    computeAllPairsShortestPath(cityCount, cost);

    int low = 0, high = 10000 * cityCount, bestDistance = high;

    while (low <= high)
    {
        int mid = (low + high) / 2;
        if (canPlaceCenters(cityCount, vaccineCenters, cost, mid))
        {
            bestDistance = mid;
            high = mid - 1;
        }
        else
        {
            low = mid + 1;
        }
    }

    cout << bestDistance << endl;
}
int main()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    solveVaccinationProblem();
    return 0;
}
