#include <iostream>
using namespace std;

int sumall(int num[], int size, int non)
{
    int sum = 0;
    for (int i = 0; i < size; i++)
    {
        if (num[i] != non)
        {
            sum += num[i];
        }
    }
    return sum;
}

// Write Your Function Here

int main()
{
    int numbers[] = {13, 20, 3, 30, 5, 7, 40, 13}; // 20 + 3 + 30 + 5 + 7 + 40 = 105
    int numssize = size(numbers);
    int noneed = 13;
    cout << sumall(numbers, numssize, noneed) << "\n";
