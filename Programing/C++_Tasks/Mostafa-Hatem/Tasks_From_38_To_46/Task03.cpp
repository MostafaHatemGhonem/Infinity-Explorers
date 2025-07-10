

#include <iostream>
using namespace std;

int main()
{
    int filling = 10;
    int vals[]{100, 200, 300, 400};

    for (int i = 0; i < 4; i++)
        vals[i] = filling;

    cout << vals[0] << "\n"; // 10
    cout << vals[1] << "\n"; // 10
    cout << vals[2] << "\n"; // 10
    cout << vals[3] << "\n"; // 10

    return 0;
}
