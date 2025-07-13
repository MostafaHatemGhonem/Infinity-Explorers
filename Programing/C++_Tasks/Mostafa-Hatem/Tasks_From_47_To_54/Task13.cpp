#include <iostream>
using namespace std;

int main()
{

    for (int i = 30; i > 1; i = i - 3)
    {
        cout << i << endl;
    }

    cout << "Without Even Numbers\n";

    for (int i = 30; i > 1; i = i - 3)
    {
        if (i % 2 != 0)
        {
            cout << i << "\n";
        }
    }
    return 0;
}