#include <sstream>
#include <vector>
#include <iostream>
using namespace std;

vector<int> parseInts(string str)
{
    vector<int> m;
    stringstream ss(str);
    char ch;
    int a;
    while (ss >> a)
    {
        m.push_back(a);
        ss >> ch;
    }

    return m;
}

int main()
{
    string str;
    cin >> str;
    vector<int> integers = parseInts(str);
    for (int i = 0; i < integers.size(); i++)
    {
        cout << integers[i] << "\n";
    }

    return 0;
}
