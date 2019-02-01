#include <iostream>

using namespace std;

auto add(int a, int b) -> int
{
    cout << "add: a=[" << a << "], b=[" << b << "]" << endl;

    return a + b;
}

int main(int argc, char** argv)
{
    cout << "TestAuto: start" <<endl;

    auto myInt = 1;
    auto myDouble = 2.2222;
    auto myStr = "This is a string.";
    cout << "myInt=[" << myInt << "]" << endl;
    cout << "myDouble=[" << myDouble << "]" << endl;
    cout << "myStr=[" << myStr << "]" << endl;

    auto myAdd = add(123, 456);
    cout << "myAdd=[" << myAdd << "]" << endl;

    cout << "TestAuto: end" << endl;

    return 0;
}

