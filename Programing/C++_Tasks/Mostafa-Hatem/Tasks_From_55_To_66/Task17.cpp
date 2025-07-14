
#include <iostream>
using namespace std;

float pricing(int phone, int phone_used, int price_new, int taxes)
{
    int price_used = price_new - 200;
    int phone_new = phone - phone_used;
    float sum_new = phone_new * price_new;
    float sum_used = phone_used * price_used;
    float total = sum_new + sum_used;

    float tax_value = total * (taxes / 100.0f);

    return total + tax_value;
}

int main()
{
    cout << pricing(50, 10, 800, 20) << "\n"; // 30400
    return 0;
}