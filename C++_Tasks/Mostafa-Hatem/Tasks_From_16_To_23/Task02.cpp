

#include <iostream>
using namespace std;

int main()
{
    double salary = 5000.98;

    cout << "Salary: " << sizeof(salary) << endl;

    long double longSalary = 5000.98;
    cout << "Long Salary: " << sizeof(longSalary) << endl;

    // 8 Bytes
    // 64 Bits
    return 0;
}