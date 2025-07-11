

#include <iostream>
using namespace std;

int main()
{
    int num1, num2;
    cout << "Num1: ";
    cin >> num1;
    cout << "Num2: ";
    cin >> num2;

    int start = num1 < num2 ? num1 : num2;
    int end = num1 > num2 ? num1 : num2;

    bool first = true;

    for (int i = start + 1; i < end; i++)
    {
        if (i % 2 != 0)
        {
            if (!first)
            {
                cout << " , ";
            }
            cout << i;
            first = false;
        }
    }

    cout << endl;

    return 0;
}
