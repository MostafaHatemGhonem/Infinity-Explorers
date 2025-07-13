#include <iostream>
using namespace std;

int main()
{

    int index = 10;
    int jump = 2;

    for (;;)
    {
        cout << index << endl;
        if (index <= 4)
        {
            break;
        }
        index = index - jump;
    }

    return 0;
}