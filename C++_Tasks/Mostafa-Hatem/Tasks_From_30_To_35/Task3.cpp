#include <iostream>
#include <string>
using namespace std;

int main()
{
    int num;
    cout << "Please Type A Number Between 0 And 150\n";
    cin >> num;
    string num_str = to_string(num);

    if (num_str.length() < 3)
    {
        num_str.insert(0, 3 - num_str.length(), '0');
    }
    cout << num_str << endl;

    // If Number Smaller Than 10 "Example 5" Output Will Be => 005
    // If Number Larger Than 10 And Smaller Than 100 "Example 59" Output Will Be => 059
    // If Number Larger Than 100 "Example 115" Output Will Be => 115

    return 0;
}