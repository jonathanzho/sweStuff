#include "TestVir.h"

#include <iostream>
#include <dlfcn.h>

using namespace std;

int main()
{
    cout << "TestTestLib: start" << endl;

    void* handle = dlopen("./libTestLib.so", RTLD_NOW);

    if (handle == NULL) {
        cout << "TestTestLib: ERROR: handle == NULL !!!" << endl;
        return 1;
    }

    typedef TestVir* create_t();
    typedef void destroy_t(TestVir* pTestVir);

    create_t* create = (create_t *) dlsym(handle, "create");
    destroy_t* destroy = (destroy_t *) dlsym(handle, "destroy");

    if (create == NULL) {
        cout << "TestTestLib: ERROR: create == NULL !!!" << endl;
        return 2;
    }

    if (destroy == NULL) {
        cout << "TestTestLib: ERROR: destroy == NULL !!!" << endl;
        return 3;
    }

    TestVir* pTestVir = create();
    pTestVir->init();
    destroy(pTestVir);

    cout << "TestTestLib: end" << endl;

    return 0;
}

