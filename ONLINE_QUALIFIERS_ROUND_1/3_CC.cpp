#include <iostream>
#include <unordered_map>
#include <vector>
#include <string>
#include <set>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int N;
    cin >> N;

    unordered_map<string, int> prefix_count;

    for (int i = 0; i < N; ++i) {
        string s;
        cin >> s;

        vector<int> freq(26, 0);
        set<string> seen;

        for (char c : s) {
            freq[c - 'a']++;

            string sig;
            for (int f : freq) {
                sig += to_string(f) + "#";  // Build signature as a string
            }

            if (!seen.count(sig)) {
                prefix_count[sig]++;
                seen.insert(sig);
            }
        }
    }

    int Q;
    cin >> Q;
    while (Q--) {
        string q;
        cin >> q;

        vector<int> freq(26, 0);
        for (char c : q) {
            freq[c - 'a']++;
        }

        string sig;
        for (int f : freq) {
            sig += to_string(f) + "#";
        }

        if (prefix_count.count(sig)) {
            cout << prefix_count[sig] << "\n";
        } else {
            cout << -1 << "\n";
        }
    }

    return 0;
}
