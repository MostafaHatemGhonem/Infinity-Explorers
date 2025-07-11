

#include <iostream>
using namespace std;

int main()
{
    // Output Needed
    cout << "For\n";
    for (int i = 10; i < 100000001; i *= i)
    {
        cout << i << endl;
    }

    cout << "While\n";
    int i = 10;
    while (i < 100000001)
    {
        cout << i << endl;
        i *= i;
    }

    return 0;
}