// compiled by:
// gcc -shared -fPIC test.c -o ctest.so

#include <stdlib.h>

float func(int N, float arr[], float x) {
    int i;
    float ans = 0;
    
    for (i = 0; i < N; i++) {
        ans += arr[i];
    }
    ans *= x;
    
    return ans;
}