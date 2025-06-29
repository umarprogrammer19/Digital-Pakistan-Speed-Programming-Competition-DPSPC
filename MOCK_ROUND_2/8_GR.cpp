#include <iostream>
#include <algorithm>
using namespace std;
long long win_in_2_rounds(long long n, int d)
{
    if (d == 1)
    {
        for (long long p = n + 1; p <= n + 100; ++p)
        {
            long long naan = n, plate = p;
            long long eat = min(naan, plate);
            naan -= eat;
            plate -= eat;

            if (naan == 0)
            {
                naan = n / 2;
            }
            else if (plate == 0)
            {
                plate = p / 2;
            }
            else
            {
                continue;
            }

            eat = min(naan, plate);
            naan -= eat;
            plate -= eat;

            if (naan == 0 && plate == 0)
            {
                return p;
            }
        }
    }
    else
    {
        for (long long p = n - 1; p > 0; --p)
        {
            long long naan = n, plate = p;
            long long eat = min(naan, plate);
            naan -= eat;
            plate -= eat;

            if (naan == 0)
            {
                naan = n / 2;
            }
            else if (plate == 0)
            {
                plate = p / 2;
            }
            else
            {
                continue;
            }

            eat = min(naan, plate);
            naan -= eat;
            plate -= eat;

            if (naan == 0 && plate == 0)
            {
                return p;
            }
        }
    }
    return -1;
}
int main()
{
    long long n;
    int d;
    cin >> n >> d;
    cout << win_in_2_rounds(n, d) << endl;
    return 0;
}
