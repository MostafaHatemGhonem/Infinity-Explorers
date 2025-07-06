

#include <iostream>
using namespace std;

int main()
{

    int num = 10;
    cout << --num << " | ";
    cout << num++;
    cout << " | " << ++num << "\n"; // 9 | 9 | 11
    cout << num++ << " | ";
    cout << num << " | " << num << "\n"; // 11 | 12 | 12
    cout << --num << " | ";
    cout << --num << " | ";
    cout << --num << "\n"; // 11 | 10 | 9

    return 0;
}
