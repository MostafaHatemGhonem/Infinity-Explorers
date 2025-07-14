
#include <iostream>
using namespace std;

float money(float price, int days)
{
    int weeks = days / 7;
    int holidays = weeks * 2;
    int working_days = days - holidays;

    cout << "Your Holidays is: " << holidays << " In All " << weeks << " weeks From " << days << " Days. \n";
    cout << "Money we want to calculate for every working day from " << working_days << " days: ";
    float per_day = price / working_days;
    cout << per_day << endl;

    return per_day;
}

int main()
{
    /*
      Hints
      21 Days Has 3 "Weeks"
      Every "Week" You Have 2 Holidays.
      Total = 3 * 2 = 6 Holidays From 21 Days
      So working days = 21 - 6 = 15
      price / working days = 2015 / 15 = 134.333...
    */
    cout << money(2015, 21) << "\n"; // ≈ 134.333
    cout << money(4500, 40) << "\n"; // ≈ 150
    return 0;
}