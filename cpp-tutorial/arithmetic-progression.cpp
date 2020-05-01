#include <bits/stdc++.h>

using namespace std;

int f(int a, int b, int n) {
    return n * (a + b) / 2;
}

int main() {
    vector<int> nums;
    int x, n;
    cin >> n;
    for (int i = 0; i < n; i++) {
        cin >> x;
        nums.push_back(x);
    }
    sort(nums.begin(), nums.end());
    cout << f(nums[0], nums[nums.size() - 1], n); 
}
