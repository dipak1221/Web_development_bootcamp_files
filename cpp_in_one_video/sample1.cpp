#include <bits/stdc++.h>
using namespace std;
int add(int a, int b)
{
    while (b != 0)
    {
        int data = (a & b);
        a = a ^ b;
        b = data << 1;
    }
    return a;
}
int main()
{
    int a = 6, b = 11;
    int sum1 = 0;
    for (int i = 1; i <= a; i++)
    {
        sum1 += add(0, b);
        cout << sum1 << endl;
    }

    cout << sum1 << endl;

    return 0;
}