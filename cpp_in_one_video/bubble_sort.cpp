#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a[] = {5, 1, 3, 6, 2};
    int count = 0;
    int l = sizeof(a) / sizeof(a[0]);
    for (int i = 0; i < l; i++)
    {
        for (int j = 0; j < l - i - 1; j++)
        {
            if (a[j] > a[j + 1])
            {
                count++;
                int temp = a[j];
                a[j] = a[j + 1];
                a[j + 1] = temp;
            }
        }
    }

    for (int i = 0; i < l; i++)
        cout << a[i] << " ";
    cout << endl
         << count << " " << endl;
    return 0;
}