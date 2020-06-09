#include <bits/stdc++.h>
using namespace std;
void bubblesort(int a[], int n)
{
    if (n <= 1)
        return;

    for (int i = 0; i < n - 1; i++)
    {
        if (a[i] > a[i + 1])
        {
            int temp = a[i];
            a[i] = a[i + 1];
            a[i + 1] = temp;
        }
    }
    bubblesort(a, n - 1);
}
int main()
{
    int a[] = {3, 8, 2, 17, 2, 7, 9};
    int n = sizeof(a) / sizeof(a[0]);
    bubblesort(a, n);

    for (int i = 0; i < n; i++)
        cout << a[i] << " ";

    return 0;
}