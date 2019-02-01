#include "MyClassFactory.h"

#include <iostream>

using namespace std;

MyClassFactory::MyClassFactory()
{
    cout << "MyClassFactory::MaClassFactory" << endl;
}

MyClassFactory::~MyClassFactory()
{
    cout << "MyClassFactory::~MyClassFactory" << endl;
}

void MyClassFactory::create(MyClass** pMyClass, int myInt)
{
    (*pMyClass) = new MyClass(myInt);
}

void MyClassFactory::destroy(MyClass** pMyClass)
{
    delete (*pMyClass);
    (*pMyClass) = NULL;
}

