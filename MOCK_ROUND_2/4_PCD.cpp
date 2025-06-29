#include <iostream>
#include <vector>
#include <cmath>
#include <algorithm>
#include <iomanip>

using namespace std;
double normalize(double angle)
{
    return fmod(fmod(angle, 360.0) + 360.0, 360.0);
}
double perfect_cover_drive(int n, double r, const vector<pair<double, double>> &fielders)
{
    vector<pair<double, double>> intervals;

    for (const auto &[x, y] : fielders)
    {
        double distance = hypot(x, y);
        if (distance <= r)
        {
            return 0.0;
        }

        double center_angle = atan2(y, x) * 180.0 / M_PI;
        double angle_offset = asin(r / distance) * 180.0 / M_PI;

        double start_angle = normalize(center_angle - angle_offset);
        double end_angle = normalize(center_angle + angle_offset);

        if (start_angle > end_angle)
        {
            intervals.emplace_back(start_angle, 360.0);
            intervals.emplace_back(0.0, end_angle);
        }
        else
        {
            intervals.emplace_back(start_angle, end_angle);
        }
    }

    sort(intervals.begin(), intervals.end());

    vector<pair<double, double>> merged;
    for (const auto &interval : intervals)
    {
        if (merged.empty() || interval.first > merged.back().second)
        {
            merged.push_back(interval);
        }
        else
        {
            merged.back().second = max(merged.back().second, interval.second);
        }
    }

    double max_gap = 0.0;
    for (size_t i = 0; i < merged.size(); ++i)
    {
        double end = merged[i].second;
        double next_start = merged[(i + 1) % merged.size()].first;

        double gap = (i == merged.size() - 1 ? next_start + 360.0 : next_start) - end;
        max_gap = max(max_gap, gap);
    }

    return round(max_gap * 1e6) / 1e6;
}
int main()
{
    int n;
    double r;
    cin >> n >> r;

    vector<pair<double, double>> fielders(n);
    for (int i = 0; i < n; ++i)
    {
        cin >> fielders[i].first >> fielders[i].second;
    }

    double result = perfect_cover_drive(n, r, fielders);
    cout << fixed << setprecision(6) << result << endl;
    return 0;
}
