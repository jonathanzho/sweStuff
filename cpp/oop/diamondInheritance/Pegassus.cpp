#include <iostream>
#include <string>

#include "Pegassus.h"

using namespace std;

Pegassus::Pegassus(string name) :
    Horse(name),
    Bird(name)
{
    cout << "Pegassus::Pegassus: name=" << name << endl;
}

Pegassus::~Pegassus() {
    cout << "Pegassus::~Pegassus" << endl;
}

void Pegassus::run() {
    cout << "Pegassus::run"  << endl;
    Horse::run();
}

