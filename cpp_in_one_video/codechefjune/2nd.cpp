#include <bits/stdc++.h>
using namespace std;
int main()
{
    int t;
    cin >> t;
    while (t--)
    {
        string s;
        cin >> s;
        int sum = 0, i = 0;
        while (i < s.length()-1)
        {
            if (s[i] == 'x' && s[i + 1] == 'y')
            {
                sum += 1;
                i += 2;
                continue;
            }
            if (s[i] == 'y' && s[i + 1] == 'x')
            {
                sum += 1;
                i += 2;
                continue;
            }
            i++;
        }

        cout << sum << endl;
    }
    return 0;
}