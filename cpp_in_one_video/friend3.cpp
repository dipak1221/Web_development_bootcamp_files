#include <bits/stdc++.h>
using namespace std;
class hello
{
public:
    int a = 5;
    friend hello operator--(hello);
};
hello operator--(hello h)
{
    hello h1;
    cout << "and";
    h1.a = h.a + 23;
    return h1;
}
void man(){
    
}
int main()
{
    hello h, h2;

    h = --h;
    cout << h.a;

    return 0;
}