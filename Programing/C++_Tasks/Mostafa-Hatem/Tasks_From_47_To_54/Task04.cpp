#include <iostream>
using namespace std;

int main()
{
    // Output Needed
    cout << "For Loop: \n";
    for (int i = 0; i < 20; i++)
    {
        if (i % 2 != 0)
            continue;
        if (i == 10 || i == 12)
            continue;
        cout << i << endl;
    }

    cout << "While Loop: \n";
    int i = 0;
    while (i < 20)
    {
        if (i % 2 != 0 || i == 10 || i == 12)
        {
            i++;
            continue;
        }
        cout << i << endl;
        i++;
    }

    return 0;
}