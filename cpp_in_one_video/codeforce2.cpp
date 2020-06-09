#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        long int n, count0 = 0, count1 = 0;
        cin >> n;
        long int a[n], b[n];
        for (long int i = 0; i < n; i++)
            cin >> a[i];
        for (long int i = 0; i < n; i++)
        {
            cin >> b[i];
            if (b[i] == 1)
                count1++;
            else
            {
                count0++;
            }
        }
        int flag = 1,flag1=1;

        if (count0 == 0 || count1 == 0)
        {
            for (long int i = 0; i < n - 1; i++)
            {
                int min = i;
                for (long int j = i + 1; j < n; j++)
                {
                    if (a[min] > a[j])
                        min = j;
                }

                if (min != i)
                {
                    flag = 0;
                    break;
                }
            }
        }
        else
        {
            flag1=0;
            cout << "Yes" << endl;
        }
        if (flag == 0)
            cout << "No" << endl;
        else if(flag1==1)
        {
            cout << "Yes" << endl;
        }
    }

    return 0;
}