#include <iostream>
#include <float.h>

using namespace std;

float FindMin(float L[], int n) {
    if (n <= 0) {
        cout << "ERROR: Array size must be greater than zero." << endl;
        return FLT_MAX;
    }
    float min = L[0];

    for (int i = 1; i < n; i++) {
        if (min > L[i]) {
            min = L[i];
        }
    }
    return min;
}

int main() {
    float L[] = {3.5, 1.2, 4.8, 0.9, 2.3};
    int n = sizeof(L) / sizeof(L[0]);

    float min = FindMin(L,n);
    if (min != FLT_MAX) {
        cout << "The minimum value is: " << min << endl;
    }

    return 0;
}