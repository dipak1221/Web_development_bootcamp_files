#include <bits/stdc++.h>
using namespace std;
int main()
{
    long int n;
    cin >> n;
    long int a[n], b[n];
    for (long int i = 0; i < n; i++)
        cin >> a[i];

    for (long int i = 0; i < n; i++)
        cin >> b[i];

    int flag = 0;
    long int count = 0, maxx = 0;
    for (long int i = 0; i < n; i++)
    {
        for (long int j = 0; j < n; j++)
        {
            if (a[j] == b[j])
            {
                count++;
            }
        }
        if (maxx < count)
            maxx = count;

        if (count == n)
        {
            flag = 1;
            break;
        }
        count = 0;
        int temp = b[n - 1];
        for (long int i = n - 1; i > 0; i--)
        {
            b[i] = b[i - 1];
        }
        b[0] = temp;
    }
    if (flag == 1)
        cout << n << endl;
    else
    {
        cout << maxx << endl;
    }

    return 0;
}