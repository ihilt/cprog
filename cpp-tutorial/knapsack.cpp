#include <bits/stdc++.h>

using namespace std;

// from https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/
// Naive recursive implementation of 0-1 knapsack problem
// Returns the maximum value that can be put in a knapsack of capacity W
int knapSack(int W, int wt[], int val[], int n)
{
    // Basis case
    if (n == 0 || W == 0) {
        return 0;
    }

    // If the weight of the nth item is more
    // than the knapsack capacity W, then
    // this item cannot be included
    // in the optimal solution
    if (wt[n-1] > W) {
        return knapSack(W, wt, val, n-1);
    }
    // Return the maximum of two cases:
    // 1. nth item included
    // 2. not included
    else {
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1), knapSack(W, wt, val, n-1));
    }
}

int main() {
    int val[] = {60, 100, 120};
    int wt[] = {10, 20, 30};
    int W = 50;
    int n = sizeof(val) / sizeof(val[0]);
    cout << knapSack(W, wt, val, n);
    return 0;
}
