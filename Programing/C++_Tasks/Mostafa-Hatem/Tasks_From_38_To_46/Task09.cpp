

#include <array>
#include <iostream>
using namespace std;

int main()
{
    int nums[] = {10, 20, 30, 40, 20, 50};

    // Method 1
    int length1 = sizeof(nums) / sizeof(nums[0]);
    cout << length1 << endl;
    // Method 2
    int length2 = std::extent<decltype(nums)>::value;
    cout << length2 << endl;
    // Method 3
    int length3 = std::size(nums);
    cout << length3 << endl;

    return 0;
}
