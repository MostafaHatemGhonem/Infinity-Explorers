
#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> nums = {5, 4, 3, 2, 1};

    // Method One

    sort(nums.begin(), nums.end());

    // Method Two

    sort(nums.rbegin(), nums.rend());
    reverse(nums.begin(), nums.end());

    // Method Three -> Use Swap + Loop For Challenge

    for (int i = 0; i < nums.size(); i++)
    {
        for (int j = 0; j < nums.size() - i - 1; j++)
        {
            if (nums[j] > nums[j + 1])
            {
                swap(nums[j], nums[j + 1]);
            }
        }
    }

    for (int i : nums)
    {
        cout << i << "\n";
    }

    return 0;
}
