#include <bits/stdc++.h>
using namespace std;

void insertion_recursion(int a[], int i, int n)
{
    //int n = 7;
    if (n == i)
        return;

    int temp = a[i];
    int j = i - 1;
    while (j >= 0 && temp < a[j])
    {
        a[j + 1] = a[j];
        j--;
    }
    a[j + 1] = temp;
    i++;
    insertion_recursion(a, i, n);
}
int main()
{
    int a[] = {118, 3, 8, 2, 0, 23, 991};
    int n = sizeof(a) / sizeof(a[0]);
    insertion_recursion(a, 1, n);

    for (int i = 0; i < n; i++)
        cout << a[i] << " ";
    return 0;
}