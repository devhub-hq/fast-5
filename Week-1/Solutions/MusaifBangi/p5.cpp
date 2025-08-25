#include <iostream>
using namespace std;
int countWays(int n) {
    if (n == 0 || n == 1) return 1;
    int prev1 = 1, prev2 = 1, curr;
    for (int i = 2; i <= n; i++) {
        curr = prev1 + prev2;
        prev2 = prev1;
        prev1 = curr;
    }
    return prev1;
}

int main() {
    int n;
    cin>>n;
    cout<<countWays(n);
    return 0;
}
