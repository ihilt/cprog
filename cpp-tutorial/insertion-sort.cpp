#include <bits/stdc++.h>

using namespace std;

void swap(int *x, int *y) {
    int tmp = *x;
    *x = *y;
    *y = tmp;
}

int main() {
    int arr[] = {3,4,12,23,4,3,2};

    for (int i = 1; i < (int)(sizeof(arr) / sizeof(arr[0])); i++) {
        int j = i;
        while ((j>0) && (arr[j] < arr[j-1])) {
            swap(&arr[j], &arr[j-1]);
            j = j-1;
        }
    }

    for (int k = 0; k < (int)(sizeof(arr) / sizeof(arr[0])); k++) {
        cout << arr[k] << "\n";
    }
}
