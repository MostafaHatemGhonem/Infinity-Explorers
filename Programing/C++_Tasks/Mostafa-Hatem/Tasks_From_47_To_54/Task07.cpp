#include <iostream>
using namespace std;

int main()
{
    // Output Needed
    cout << "For\n";
    for (int i = 2; i < 129; i *= 2)
    {
        cout << i << endl;
    }

    cout << "While\n";
    int i = 2;
    while (i < 129)
    {
        cout << i << endl;
        i *= 2;
    }

    return 0;
}