#include <iostream>
using namespace std;

string swapping(string text)
{
    for (int i = 0; i < text.length(); ++i)
    {
        if (text[i] == 'H')
        {
            continue;
        }
        else if (isupper(text[i]))
        {
            text[i] = tolower(text[i]);
        }
        else if (islower(text[i]))
        {
            text[i] = toupper(text[i]);
        }
    }
    return text;
}

int main()
{
    cout << swapping("hero Of THe PROgramming") << "\n"; // hERO oF tHE proGRAMMING
    return 0;
}
