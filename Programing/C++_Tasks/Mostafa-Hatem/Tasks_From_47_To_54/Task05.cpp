

#include <iostream>
using namespace std;

int main()
{
    // Output Needed
    cout << "For\n";
    for (int i = 0; i < 30; i += 3)
    {
        cout << i << endl;
    }

    cout << "While\n";
    int i = 0;
    while (i < 30)
    {
        cout << i << endl;
        i += 3;
    }

    return 0;
}
