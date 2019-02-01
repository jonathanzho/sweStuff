#include "MyClass.h"

#include <iostream>

using namespace std;

MyClass::MyClass(int myInt) :
    m_myInt(myInt)
{
    cout << "MyClass::MyClass: m_myInt=[" << m_myInt << "]" << endl;
}

MyClass::~MyClass()
{
    cout << "MyClass::~Myclass: m_myInt=[" << m_myInt << "]" << endl;
}

int MyClass::getInt()
{
    cout << "MyClass::getInt. m_myInt=[" << m_myInt << "]" << endl;

    return m_myInt;
}

void MyClass::sMethod(int myInt)
{
    cout << "MyClass::sMethod: myInt=[" << myInt << "]" << endl;
}

