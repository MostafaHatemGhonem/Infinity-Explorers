
#include <iostream>
#include <string>
using namespace std;

int main()
{
    int age = 40;
    int points = 100;

    if (age > 18)
    {
        cout << "Age Is Ok\n";
        if (points > 50)
        {
            cout << "Points Is Ok\n";
            if (sizeof(age) == 4)
            {
                cout << "Age Data Is 4 Bytes\n";
            }
        }
    }

    cout << (age > 18 ? "Age Is Ok\n" : "");
    cout << (points > 50 ? "Points Is Ok\n" : "");
    cout << (sizeof(age) == 4 ? "Age Data Is 4 Bytes\n" : "");
