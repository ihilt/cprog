#include <bits/stdc++.h>

using namespace std;

void print_arr(vector<int>& arr) {
    for (int i = 0; i < (int)arr.size(); i++) {
        cout << arr[i] << endl;
    }
}

int subarraySum(vector<int>& nums) {
    int answer = 0;
    vector<int> dp;
    int pref = 0;
    for (int i = 0; i < (int)nums.size(); i++) {
        pref += nums[i];
        dp.push_back(pref);
    }
    print_arr(dp);
    return answer;
}

int main() {
    vector<int> nums;
    int n;

    cin >> n;

    for (int i = 0; i < n; i++) {
        int j;
        cin >> j;
        nums.push_back(j);
    }
    cout << subarraySum(nums);
}
