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

    int even_a = a >> 1;
    int even_b = b >> 1;

    int odd_a = a - even_a;
    int odd_b = b - even_b;

    cout << odd_a*odd_b + even_a*even_b << endl;
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