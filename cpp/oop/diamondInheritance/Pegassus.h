#ifndef PEGASSUS
#define PEGASSUS

#include <iostream>
#include <string>

#include "Horse.h"
#include "Bird.h"

using namespace std;

class Pegassus : public Horse, public Bird {
public:
    Pegassus(string name);
    ~Pegassus();
public:
    void run();
};

#endif // PEGASSUS
