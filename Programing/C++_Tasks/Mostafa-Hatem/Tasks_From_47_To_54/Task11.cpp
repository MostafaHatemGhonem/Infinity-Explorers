
#include <iostream>
using namespace std;

int main()
{
    string friends[] = {"Ahmed", "Osama", "Ameer", "Mostafa"};
    int length_all = sizeof(friends) / sizeof(friends[0]);

    for (int i = 0; i < length_all; i++)
    {
        for (int k = 0; k < length_all + 2; k++)
        {
            cout << "==";
        }
        cout << endl;
        cout << " = " << friends[i] << " = \n";

        int length = friends[i].size();

        for (int k = 0; k < length + 2; k++)
        {
            cout << "==";
        }
        cout << endl;
        cout << "= ";
        for (int j = 0; j < length; j++)
        {
            cout << friends[i][j];
            if (j != length - 1)
            {
                cout << ",";
            }
        }
        cout << " =\n";
        for (int k = 0; k < length + 2; k++)
        {
            cout << "==";
        }
        cout << endl;
        cout << endl;
    }
    return 0;
}