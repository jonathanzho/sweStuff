#ifndef ANIMAL
#define ANIMAL

#include <iostream>
#include <string>

using namespace std;

class Animal {
private:
    string mName;
public:
    Animal(string name);
    virtual ~Animal();
public:
    string getName();
    void setName(string name);
};

#endif // ANIMAL

