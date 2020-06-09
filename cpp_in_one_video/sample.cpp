#include <bits/stdc++.h>
using namespace std;
class hello
{
public:
    void operator-()
    {
        cout << "hello";
    }
};

int main()
{
    hello h;
    -h;
    return 0;
}