#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main()
{
    vector<int> numbers = {10, 20, 30, 40, 50, 60, 70, 80};
    vector<int>::iterator it = numbers.begin();

    // Write Method One
    advance(it, distance(numbers.begin(), numbers.end()) / 2 - 1);
    cout << *it << endl;
    // Write Method Two
    it = numbers.begin() + (numbers.end() - numbers.begin()) / 2 - 1;
    cout << *it << endl;

    // Write Method Three
    it = next(numbers.begin(), (numbers.size() / 2) - 1);
    cout << *it << endl;

    return 0;
}