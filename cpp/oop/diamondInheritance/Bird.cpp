#include <iostream>
#include <string>

#include "Bird.h"

using namespace std;

Bird::Bird(string name) :
    Animal(name)
{
    cout << "Bird::Bird: name=" << name << endl;
}

Bird::~Bird() {
    cout << "Bird::~Bird" << endl;
}

void Bird::fly() {
    cout << "Bird::fly" << endl;
}

void Bird::run() {
    cout << "Bird::run: 2 legs"  << endl;
}

