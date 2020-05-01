#include <bits/stdc++.h>

using namespace std;

int main() {
    int n = 8;
    vector<int> adj[n];
    adj[1].push_back(2);
    adj[2].push_back(3);
    adj[2].push_back(4);
    adj[3].push_back(4);
    adj[4].push_back(1);
    
    for (int b : adj[2]) {
        cout << b;
    }
}
