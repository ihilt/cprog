#include <bits/stdc++.h>

using namespace std;

/**
 * Main assumption which drives code: subarraysum[L..R] == pref[R] - pref[L-1]
 * k = subarraysum[L..R]
 * pref[L-1] = pref[R] - k
 *
 * Then, we count the occurances of pref[L-1] since those indicate the position in the array where
 * the sum up to pref[R] is equal to k.
 * answer is used to increment the number of times k is seen in countPref.
 * pref is the prefix sum equal to pref[R] in the description above.
 *
 * This also works for negative subarray sums.
 */
int subarraySum(vector<int>& nums, int k) {
    int n = nums.size();
    int answer = 0;
    int pref = 0;
    unordered_map<int, int> countPref;
    countPref[pref]++;
    for(int R = 0; R < n; R++) {
        pref += nums[R];
        int need = pref - k;
        answer += countPref[need];
        countPref[pref]++;
    }
    return answer;
}

int main() {
    vector<int> nums;
    int k, n;

    cin >> n;
    cin >> k;

    for (int i = 0; i < n; i++) {
        int j;
        cin >> j;
        nums.push_back(j);
    }
    cout << subarraySum(nums, k);
}
