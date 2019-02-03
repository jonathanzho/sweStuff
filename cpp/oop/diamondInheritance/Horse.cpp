#include <iostream>
#include <string>

#include "Horse.h"

using namespace std;

Horse::Horse(string name) :
    Animal(name)
{
    cout << "Horse::Horse: name=" << name << endl;
}

Horse::~Horse() {
    cout << "Horse::~Horse" << endl;
}

void Horse::run() {
    cout << "Horse::run: 4 legs"  << endl;
}

