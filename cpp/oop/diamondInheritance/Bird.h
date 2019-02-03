#ifndef BIRD
#define BIRD

#include <iostream>
#include <string>

#include "Animal.h"

using namespace std;

class Bird : public Animal {
public:
    Bird(string name);
    virtual ~Bird();
public:
    virtual void fly();
    virtual void run();
};

#endif // BIRD

