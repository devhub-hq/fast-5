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

    vector<int> a (n);
    for (auto& x : a)
    {
        cin >> x;
    }

    if (n == 1)
    {
        cout << a[0] << endl;
        return;
    }

    int two_step_back = a[0];        
    int one_step_back = max (a[0], a[1]);

    if (n == 2)
    {
        cout << one_step_back << endl;
        return;
    }

    int max_energy = 0;
    for (int i = 2; i < n; ++i)
    {
        max_energy = max(one_step_back, a[i] + two_step_back);

        two_step_back = one_step_back;
        one_step_back = max_energy;
    }

    cout << max_energy << endl;
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