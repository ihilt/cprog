#include <bits/stdc++.h>

using namespace std;

vector<int> bubblesort(vector<int> ar) {
    for (int i = 0; i < ar.size(); i++) {
        if (i+1 == ar.size()) break;
        if (ar[i] > ar[i+1]) {
            int tmp = ar[i];
            ar[i] = ar[i+1];
            ar[i+1] = tmp;
        }
    }
    return ar;
}

int main() {
    vector<int> arr;
    int n;

    cin >> n;

    for (int i = 0; i < n; i++) {
        int j;
        cin >> j;
        arr.push_back(j);
    }

    for (int i = 0; i < n; i++) {
        if (i+1 == arr.size()) break;
        if (arr[i] > arr[i+1]) {
            arr = bubblesort(arr);
            i = -1;
        }
    }

    for (int i = 0; i < n; i++) {
        cout << arr[i];
    }
}
