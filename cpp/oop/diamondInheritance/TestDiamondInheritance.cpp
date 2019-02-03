#include <iostream>

#include "Animal.h"
#include "Bird.h"
#include "Horse.h"
#include "Pegassus.h"

using namespace std;

int main(void) {
    cout << "========== new animal1" <<endl;
    Animal* pAnimal1 = new Animal("animal1");

    cout << "========== new bird2" <<endl;
    Bird* pBird2 = new Bird("bird2");
    pBird2->fly();
    pBird2->run();

    cout << "========== new horse3" <<endl;
    Horse* pHorse3 = new Horse("horse3");
    pHorse3->run();

    cout << "========== new pegassus4" <<endl;
    Pegassus* pPegassus4 = new Pegassus("pegassus4");
    pPegassus4->fly();
    pPegassus4->run();

    cout << "========== delete animal1" <<endl;
    delete pAnimal1;

    cout << "========== delete bird2" <<endl;
    delete pBird2;

    cout << "========== delete horse3" <<endl;
    delete pHorse3;

    cout << "========== delete pegassus4" <<endl;
    delete pPegassus4;

    return 0;
}
