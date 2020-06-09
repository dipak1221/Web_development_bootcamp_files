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
    long int min = b[0] / a[0];
    
    for (long int i = 1; i < n; i++)
    {
        long int f = b[i] / a[i];
        if (min > f)
        {
            min = f;
        }
    }
    cout << min<<endl;
    return 0;
}