

#include <iostream>
using namespace std;

int main()
{
    double salary = 5000.98;

    cout << "Salary: " << sizeof(salary) << " bytes" << endl;
    cout << "Salary: " << sizeof(salary) * 8 << " Bites" << endl;

    // 8 Bytes
    // 64 Bits
    return 0;
}