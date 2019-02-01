#include "MyClass.h"

class MyClassFactory {
public:
    MyClassFactory();
    ~MyClassFactory();
public:
    static void create(MyClass** pMyClass, int myInt);
    static void destroy(MyClass** pMyClass);
};

