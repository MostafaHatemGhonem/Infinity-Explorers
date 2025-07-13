
#include <iostream>
using namespace std;

int main()
{

    string names[] = {"Osama", "Ahmed", "Mahmoud", "Hagar", "Eman", "Salwa"};
    int length_names = sizeof(names) / sizeof(names[0]);

    for (int i = 0; i < length_names; i++)
    {
        if (size(names[i]) == 5)
        {
            cout << names[i] << endl;
        }
        cout << "";
    }

    return 0;
}