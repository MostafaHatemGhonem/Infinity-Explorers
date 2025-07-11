
#include <array>
#include <iostream>
using namespace std;

int main()
{
    cout << "// For Output\n";
    for (int i = 0; i < 11; i++)
    {
        cout << i << endl;
    }

    cout << "// While Output\n";
    int i = 0;
    while (i < 11)
    {
        cout << i << endl;
        i++;
    }

    cout << "// Do While Output\n";
    i = 0;
    do
    {
        cout << i << endl;
        i++;
    } while (i < 11);
    return 0;
}