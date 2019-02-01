#include "TestLib.h"

#include <iostream>

using namespace std;

void TestLib::init()
{
    cout << "TestLib::init" << endl;
}

// Define functions with C symbols: create/destroy TestLib instance

extern "C" TestLib* create()
{
    cout << "create TestLib" << endl;

    return new TestLib();
}

extern "C" void destroy(TestLib* pTestLib)
{
    cout << "destroy TestLib" << endl;

    delete pTestLib;
    pTestLib = NULL;
}

