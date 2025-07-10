
#include <array>
#include <iostream>
using namespace std;

int main()
{
    string fName = "Elzero ";
    string mName = "Web ";
    string lName = "School";

    string arrayNames[] = {fName, mName, lName};
    int length = sizeof(arrayNames) / sizeof(arrayNames[0]);
    // Output Needed
    cout << fName << mName << lName << endl;
    cout << arrayNames[0] << arrayNames[1] << arrayNames[2] << endl;
    for (int i = 0; i < length; i++)
    {
        cout << arrayNames[i];
    }
    return 0;
}