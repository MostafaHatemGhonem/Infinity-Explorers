#include <iostream>
using namespace std;

int main()
{

    int num = 2;
    while (num < 520)
    {
        num = num - 1;
        cout << num << "\n";
        num = ((num * 2) + 3);
    }

    return 0;
}