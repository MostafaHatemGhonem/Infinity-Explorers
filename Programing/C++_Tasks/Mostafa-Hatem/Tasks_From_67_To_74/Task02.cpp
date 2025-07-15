#include <iostream>
#include <vector>
using namespace std;

int main()
{
    vector<int> numbers = {10, 20, 30, 40};
    cout << numbers[0] << endl;
    cout << numbers.at(0) << endl;
    cout << numbers.front() << endl;
    cout << numbers[numbers.size() - numbers.size()] << endl;
    cout << *numbers.begin() << endl;

    cout << "\n===================\n";

    cout << numbers[3] << endl;
    cout << numbers.at(3) << endl;
    cout << numbers.back() << endl;
    cout << numbers[numbers.size() - 1] << endl;

    return 0;
}