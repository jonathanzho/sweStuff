#!/bin/sh

g++ -Wall -g -c TestDiamondInheritance.cpp
g++ -Wall -g   -c -o Animal.o Animal.cpp
g++ -Wall -g   -c -o Horse.o Horse.cpp
g++ -Wall -g   -c -o Bird.o Bird.cpp
g++ -Wall -g   -c -o Pegassus.o Pegassus.cpp
g++ -Wall -g -o TestDiamondInheritance TestDiamondInheritance.o Animal.o Horse.o Bird.o Pegassus.o

