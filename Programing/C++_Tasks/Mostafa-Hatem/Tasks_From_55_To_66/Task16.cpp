#include <iostream>
using namespace std;

int books(int small, int mid, int large, int all)
{
    small *= 2;
    mid *= 4;
    large *= 6;
    all *= 20;
    int sum = small + mid + large;
    if (sum < all)
    {
        return all - sum;
    }
    else
    {
        return 0;
    }
}

int main()
{
    cout << books(10, 4, 3, 4) << "\n"; // 26
    cout << books(10, 4, 3, 2) << "\n"; // 0
    return 0;
}