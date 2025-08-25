#include <bits/stdc++.h>

#define int long long
#define MAX LLONG_MAX
#define MIN LLONG_MIN

using namespace std;

int ceil (int a, int b)
{
    return (a + b - 1)/b;
}

void solve (int testCaseId)
{
    int n;
    cin >> n;

    int r = 0;
    for (int i = 0; i < n; ++i)
    {
        int x;
        cin >> x;

        r ^= x;
    }

    cout << r << endl;
}

int32_t main()
{
    int totalNumberOfTestCases = 1;
    //cin >> totalNumberOfTestCases;

    for (int testCaseId = 0; testCaseId < totalNumberOfTestCases; ++testCaseId)
    {
        solve (testCaseId);
    }

    return 0;
}