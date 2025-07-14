#include <iostream>
#include <climits>
using namespace std;
int minpositive(int num[], int size)
{
    int min = INT_MAX;
    for (int i = 0; i < size; i++)
    {
        if (num[i] > 0)
        {
            if (num[i] < min)
            {
                min = num[i];
            }
        }
    }
    return min;
}
// Write Your Function Here

int main()
{
    int numbers[] = {-10, -20, 15, 100, 10, 5, -50, 0}; // 5
    int numssize = size(numbers);
    cout << minpositive(numbers, numssize) << "\n";
    return 0;
}