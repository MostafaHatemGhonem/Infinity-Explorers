
#include <iostream>
using namespace std;

int main()
{
    int check = 25;
    int nums[]{40, 20, 30, 70, 100};
    int length = sizeof(nums) / sizeof(nums[0]);

    for (int i = 0; i < length; ++i)
    {
        if (nums[i] > check)
        {
            cout << nums[i] << " + " << nums[length - 2] << " = " << nums[i] + nums[length - 2] << endl;
        }
    }

    return 0;
}