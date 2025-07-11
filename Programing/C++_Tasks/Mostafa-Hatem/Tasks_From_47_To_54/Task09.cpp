

#include <iostream>
using namespace std;

int main()
{
    string friends[] = {"Ahmed", "Mohamed", "Sayed", "Gamal"};
    cout << "For: \n";
    for (int i = 1; i < 3; i++)
    {
        cout << friends[i] << endl;
    }

    cout << "While: \n";
    int i = 1;
    while (i < 3)
    {
        cout << friends[i] << endl;
        i++;
    }

    return 0;
}
