#ifndef HORSE
#define HORSE

#include <iostream>
#include <string>

#include "Animal.h"

using namespace std;

class Horse : public Animal {
public:
    Horse(string name);
    virtual ~Horse();
public:
    virtual void run();
};

#endif // HORSE

