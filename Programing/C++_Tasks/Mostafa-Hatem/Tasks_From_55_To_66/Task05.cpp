#include <iostream>
using namespace std;

void thepower(int num1, int num2)
{
    cout << exp(num2 * log(num1));
}

// Write Your Function Here

int main()
{
    thepower(2, 5); // 32
    return 0;
}