
#include <iostream>
using namespace std;

int main()
{
    string friends[] = {"Ahmed", "Mohamed", "ameer", "Ashraf", "Amany"};
    int length = sizeof(friends) / sizeof(friends[0]);

    cout << "Using For Loop: " << endl;
    for (int i = 0; i < length; i++)
    {
        if (friends[i][0] == 'A')
        {
            cout << friends[i] << endl;
        }
    }
    cout << "Using While Loop: " << endl;
    int i = 0;
    while (i < length)
    {
        if (friends[i][0] == 'A')
        {
            cout << friends[i] << endl;
        }
        i++;
    }
    return 0;
}