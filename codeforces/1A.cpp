#include <bits/stdc++.h>

using namespace std;

int main() {
    long long n, m, a;

    cin >> n;
    cin >> m;
    cin >> a;

    if (n <= a && m <= a) {
        cout << 1;
        return 0;
    }
    cout << ((m+a-1) / a) * ((n+a-1) / a);
}
