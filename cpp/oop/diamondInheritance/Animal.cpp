#include <iostream>
#include <string>

#include "Animal.h"

using namespace std;

Animal::Animal(string name) {
    cout << "Animal::Animal: name=" << name << endl;
    mName = name;
}

Animal::~Animal() {
    cout << "Animal::~Animal" << endl;
}

string Animal::getName() {
    cout << "Animal::getName: mName=" << mName << endl;
    return mName;
}

void Animal::setName(string name) {
    cout << "Animal::setName: name=" << name << endl;
    mName = name;
}

