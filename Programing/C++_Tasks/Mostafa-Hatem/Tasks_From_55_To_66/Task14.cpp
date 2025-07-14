#include <iostream>
using namespace std;

int calculate(float num1, float num2, string op = "")
{
    if (op == "multiply" || op == "m")
    {
        return num1 * num2;
    }
    else if (op == "subtract" || op == "s")
    {
        return num1 - num2;
    }
    else if (op == "add" || op == "a")
    {
        return num1 + num2;
    }
    else if (op == "")
    {
        return num1 + num2;
    }
    else
    {
        return 0;
    }
}

int main()
{
    cout << calculate(10, 20) << "\n";             // 30
    cout << calculate(10, 20, "a") << "\n";        // 30
    cout << calculate(10, 20, "s") << "\n";        // -10
    cout << calculate(10, 20, "subtract") << "\n"; // -10
    cout << calculate(10, 20, "multiply") << "\n"; // 200
    cout << calculate(10, 20, "m") << "\n";        // 200
    cout << calculate(10, 20, "Invalid") << "\n";  // 0
    return 0;
}