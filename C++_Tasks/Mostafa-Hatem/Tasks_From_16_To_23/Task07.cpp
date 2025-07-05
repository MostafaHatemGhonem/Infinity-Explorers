// int a = 1;
// int b = 13;
// int c = 17;
// int d = 70;

// // Output Needed
// "EWS"

#include <iostream>
using namespace std;

int main()
{
    int a = 1;
    int b = 13;
    int c = 17;
    int d = 70;

    // Convert integers to characters
    char firstChar = char(d - a);
    char secondChar = char(c + d);
    char thirdChar = char(b + d);
    cout << firstChar << secondChar << thirdChar << endl; // Output: EWS

    return 0;
}