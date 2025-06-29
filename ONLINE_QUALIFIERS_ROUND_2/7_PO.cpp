#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
int minimizeProjectTime(int n, vector<int> &mainTime, vector<int> &altTime,
                        vector<int> &switchToAlt, vector<int> &switchToMain,
                        int mainStart, int altStart, int mainDeploy, int altDeploy)
{

    vector<int> dpMain(n), dpAlt(n);
    dpMain[0] = mainStart + mainTime[0];
    dpAlt[0] = altStart + altTime[0];
    for (int i = 1; i < n; ++i)
    {
        dpMain[i] = min(
            dpMain[i - 1] + mainTime[i],                 
            dpAlt[i - 1] + switchToMain[i] + mainTime[i] 
        );

        dpAlt[i] = min(
            dpAlt[i - 1] + altTime[i],                  
            dpMain[i - 1] + switchToAlt[i] + altTime[i] 
        );
    }
    return min(dpMain[n - 1] + mainDeploy, dpAlt[n - 1] + altDeploy);
}
int main()
{
    int n;
    cin >> n;

    vector<int> mainTime(n), altTime(n);
    vector<int> switchToAlt(n), switchToMain(n);

    for (int i = 0; i < n; ++i)
        cin >> mainTime[i];
    for (int i = 0; i < n; ++i)
        cin >> altTime[i];
    for (int i = 0; i < n; ++i)
        cin >> switchToAlt[i];
    for (int i = 0; i < n; ++i)
        cin >> switchToMain[i];

    int mainStart, altStart, mainDeploy, altDeploy;
    cin >> mainStart >> altStart >> mainDeploy >> altDeploy;

    int result = minimizeProjectTime(n, mainTime, altTime,
                                     switchToAlt, switchToMain,
                                     mainStart, altStart, mainDeploy, altDeploy);
    cout << result << endl;
    return 0;
}
