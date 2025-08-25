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
    int a, b;
    cin >> a >> b;

    int difference = abs(a - b);

    cout << difference/10 + bool(difference%10) << endl;
}

int32_t main()
{
    int totalNumberOfTestCases = 1;
    cin >> totalNumberOfTestCases;

    for (int testCaseId = 0; testCaseId < totalNumberOfTestCases; ++testCaseId)
    {
        solve (testCaseId);
    }

    return 0;
}