#include <bits/stdc++.h>

using namespace std;

int f(int a, int b, int k) {
    return ((b * k) - a) / (k - 1);
}

int main() {
    vector<int> nums;
    int x, n, k;
    cin >> n;
    cin >> k;
    for (int i = 0; i < n; i++) {
        cin >> x;
        nums.push_back(x);
    }
    sort(nums.begin(), nums.end());
    cout << f(nums[0], nums[nums.size() - 1], k); 
}
