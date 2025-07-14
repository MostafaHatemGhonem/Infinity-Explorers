#include <iostream>
using namespace std;
string createurl(string prot = "https", string name = "Mostafa", string domain = "com", bool www = true)
{
    if (www)
    {
        return prot + "://www." + name + "." + domain;
    }
    else
    {
        return prot + "://" + name + "." + domain;
    }
}

// Write Your Function Here

int main()
{
    cout << createurl("https", "elzero", "org") << "\n";        // https://www.elzero.org
    cout << createurl("https", "google", "com", false) << "\n"; // https://google.com
    cout << createurl("http", "learn", "net") << "\n";          // http://www.learn.net
    cout << createurl();
    return 0;
}