#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        int n, k, sum = 0;
        cin >> n;
        cin >> k;
        int a[n];
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            if (a[i] > k)
                sum += a[i] - k;
        }
        cout << sum << endl;
    }
    return 0;
    
}
