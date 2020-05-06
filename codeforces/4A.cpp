#include <bits/stdc++.h>

using namespace std;

int main() {
    int w;

    cin >> w;

    if (w < 4) {
        cout << "NO";
    } else if (w % 2 != 0) {
        cout << "NO";
    } else {
        for (int i = 2; i < w; i += 2) {
            if ((w - i) % 2 == 0) {
                cout << "YES";
                return 0;
            }
        }
        cout << "NO";
    }
}
