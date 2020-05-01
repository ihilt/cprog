#include <bits/stdc++.h>

using namespace std;

int main() {
    int a, b;

    cin >> a >> b;

    int r_and_b_days = min(a, b);
    int same_color_days = (max(a, b) - min(a, b)) / 1;
    cout << r_and_b_days << " " << same_color_days;
}
