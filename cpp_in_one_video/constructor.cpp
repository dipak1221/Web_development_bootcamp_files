#include <bits/stdc++.h>
using namespace std;
class con
{

public:
    int a;
    int operator--(int)
    {

        cout << "hello operator overloading" << endl;
        return a;
    }
};
int main()
{
    con c1;
    c1.a = 45;
    cout << c1-- << endl;
    return 0;
}
