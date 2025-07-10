

#include <iostream>
using namespace std;

int main()
{
    // Example 1
    int vals[]{100, 200, 500, 400, 200};

    if (vals[0] + vals[1] > vals[2])
    {
        cout << "First Number + Second Number Is Larger Than Middle Number\n";
        cout << vals[0] << " + " << vals[1] << " = " << vals[0] + vals[1] << "\n";
        cout << vals[0] + vals[1] << " > " << vals[2] << "\n";
    }
    else if (vals[0] + vals[4] > vals[2])
    {
        cout << "Second Number + Before Last Number Is Larger Than Middle Number\n";
        cout << vals[0] << " + " << vals[4] << " = " << vals[0] + vals[4] << "\n";
        cout << vals[0] + vals[4] << " > " << vals[2] << "\n";
    }
    else
    {
        cout << "Middle Number Is The Largest\n";
        cout << vals[2] << "\n";
    }

    return 0;
}
