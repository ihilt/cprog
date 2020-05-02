#include <bits/stdc++.h>

using namespace std;

int minmax(vector<int>& coins, int prefhalf) {
    int n = (int)coins.size();
    int answer = 0;

    sort(coins.rbegin(), coins.rend());

    for (int i = 0; i < n; i++) {
        int cursum = 0;
        for (int j = i; j < n; j++) {
            answer++;
            cursum += coins[j];
            if (cursum > prefhalf) {
                return answer;
            }
        }
    }
    return answer;
}

int main() {
    int n;

    vector<int> coins;
    int prefsum = 0;

    cin >> n;

    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        coins.push_back(k);
        prefsum += k;
    }

    cout << minmax(coins, prefsum / 2);
}
