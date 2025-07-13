#include <iostream>
using namespace std;

int main()
{

    int help_num = 4;
    int nums[] = {2, 4, 5, 6, 10};

    int length = sizeof(nums) / sizeof(nums[0]);
    for (int i = 0; i < length; i++)
    {
        cout << nums[i] << " + ";
        cout << nums[help_num - i] << " = ";
        cout << nums[i] + nums[help_num - i] << endl;
    }

    return 0;
}
