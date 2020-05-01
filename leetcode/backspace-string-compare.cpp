#include <bits/stdc++.h>

using namespace std;

bool backspaceCompare(S, T) {
    if (S == T) {
        return true;
    }
    int i = 0;
    while (i < S.length()) {
        if (i == 0 and S[i] == "#") {
            S = S.substr(1, S.length());
            continue;
        }
        if (S[i] == "#") {
            S = S[0:i - 1] + S[i + 1:];
            
            i -= 2;
        }
        i += 1;
        if (i < 0) {
            break;
        }
    }

    i = 0;
    while (i < len(T)) {
        if i == 0 and T[i] == "#":
            T = T[1:]
            continue
        if T[i] == "#":
            T = T[0:i - 1] + T[i + 1:]
            i -= 2
        i += 1
        if i < 0:
            break
    }

    if (T != S) {
        return false;
    }
    return true;
}

int main() {
    string S, T;

    cin >> S;
    cin >> T;

    cout << backspaceCompare(S, T);
}
