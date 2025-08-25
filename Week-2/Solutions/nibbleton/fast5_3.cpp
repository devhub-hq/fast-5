#include <bits/stdc++.h>

#define int long long
#define MAX LLONG_MAX
#define MIN LLONG_MIN

using namespace std;

int ceil (int a, int b)
{
    return (a + b - 1)/b;
}

int get_digit_square_sum (int n)
{
    int digit_square_sum = 0;
    while (n)
    {
        int d = n%10;
        digit_square_sum += d*d;
        n /= 10;
    }
    return digit_square_sum;
}

string is_valid (int n)
{
    set<int> already_seen;
    while (n != 1 and not already_seen.count(n))
    {
        already_seen.insert (n);
        n = get_digit_square_sum (n);
    }

    return n == 1 ? "true" : "false";
}

void solve (int testCaseId)
{
    int n;
    cin >> n;

    cout << is_valid (n) << endl;
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