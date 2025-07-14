
#include <iostream>
#include <string>
using namespace std;

string plusandmultiply(int num[], int size)
{
    int even = 0;
    int odd = 1;
    for (int i = 0; i < size; i++)
    {
        if (num[i] % 2 == 0)
        {
            even += num[i];
        }
        else
        {
            odd *= num[i];
        }
    }

    return string("Even Numbers: ") + to_string(even) + "\nOdd Numbers: " + to_string(odd);
}

// Write Your Function Here

int main()
{
    int numbers[] = {10, 20, 3, 30, 5, 7, 40};
    int numssize = size(numbers);
    cout << plusandmultiply(numbers, numssize) << "\n";
    // Even Numbers -> 10 + 20 + 30 + 40 = 100
    // Odd Numbers  -> 3 * 5 * 7 = 105
    // Total = 100 + 105 = 205
    return 0;
}