#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;

    while (t--)
    {
        int n, sum = 0;
        cin >> n;
        int a[n], flag = 0;
        for (int i = 0; i < n; i++)
        {
            cin >> a[i];
            if (a[i] == 5)
                sum += 1;
            if (a[i] == 10)
                sum -= 1;
            if (a[i] == 15)
                sum -= 2;

            if (sum < 0)
            {
                flag = 1;
            }
        }
        if (flag == 0)
        {
            cout << "YES" << endl;
        }
        else
        {
            cout << "NO" << endl;
        }
    }
    return 0;
}
