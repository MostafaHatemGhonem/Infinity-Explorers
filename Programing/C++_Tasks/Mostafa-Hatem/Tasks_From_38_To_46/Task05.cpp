

#include <iostream>
using namespace std;

int main()
{
    int vals[] = {100, 200, 600, 200, 100};
    int length = sizeof(vals) / sizeof(vals[0]);
    bool is_palindrome = true;

    for (int i = 0; i < length / 2; i++)
    {
        if (vals[i] != vals[length - i - 1])
        {
            is_palindrome = false;
            break;
        }
    }

    if (is_palindrome)
    {
        cout << "Array Is Palindrome" << endl;
    }
    else
    {
        cout << "Array Is Not Palindrome" << endl;
    }

    return 0;
}
