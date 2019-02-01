#include "MyClassFactory.h"

#include <iostream>

using namespace std;

int main(void)
{
    cout << "TestMyClass start" << endl;

    MyClass* pMyClass1 = new MyClass(1);

    pMyClass1->getInt();
    MyClass::sMethod(11);
    pMyClass1->sMethod(111);

    delete pMyClass1;

    MyClass* pMyClass2 = NULL;
    MyClassFactory::create(&pMyClass2, 2);

    pMyClass2->getInt();
    MyClass::sMethod(22);
    pMyClass2->sMethod(222);

    MyClassFactory::destroy(&pMyClass2);

    cout << "TestMyClass end" << endl;
}

