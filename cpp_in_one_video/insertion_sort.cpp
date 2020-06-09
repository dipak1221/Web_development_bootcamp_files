#include <bits/stdc++.h>
using namespace std;
int main()
{
    int a[] = {3, 1, 2, 7, 3};
    int l = sizeof(a) / sizeof(a[0]);

    for (int i = 1; i < l; i++)
    {
        int temp = a[i];
        int j = i - 1;
        while (j >= 0 && a[j] > temp)
        {
            a[j + 1] = a[j];
            j--;
        }
        a[j + 1] = temp;
    }

    for(int i=0;i<l;i++)
    cout<<a[i]<<" ";
    return 0;
}