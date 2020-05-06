#include <bits/stdc++.h>

using namespace std;

int main() {
    int n;
    vector<int> nums;
    int best = 0;
    int answer = 0;

    cin >> n;
    for (int i = 0; i < n; i++) {
        int k;
        cin >> k;
        nums.push_back(k);
        best = max(k, best);
    }
    
    for (int i = 0; i < n; i++) {
        answer += best - nums[i];
    }

    cout << answer;
}
