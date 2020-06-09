#include <bits/stdc++.h>
using namespace std;
class demo
{
private:
    int a, b;

public:
    void set(int aa, int bb)
    {
        a = aa;
        b = bb;
    }
    void showData()
    {
        cout << a << " " << b << endl;
    }
};
int main()
{
    demo m1, m2;
    m1.set(4, 7);
    // m2.set(6, 2);
    m2.showData();

    return 0;
}
