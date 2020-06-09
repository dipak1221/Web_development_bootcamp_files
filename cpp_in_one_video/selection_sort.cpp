#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a[] = {6, 5, 4, 3, 2, 1};
    int n = sizeof(a) / sizeof(a[0]);

    for (int i = 0; i < n - 1; i++)
    {
        int min = i;
        for (int j = i + 1; j < n; j++)
        {
            if (a[min] > a[j])
            {
                min = j;
            }
        }
        if (min != i)
        {
            int temp = a[min];
            a[min] = a[i];
            a[i] = temp;
        }
    }

    for (int i = 0; i < n; i++)
        cout << a[i] << " ";

    return 0;
}