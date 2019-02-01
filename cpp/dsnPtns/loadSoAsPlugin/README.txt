This shows how to load a C++ shared library at run-time using dlopen() and resolve function symbols at run-time using dlsym().

class TestLib: actual feature class.
class TestVir: wrapper class for TestLib.
main.cpp: driver app to test TestLib via TestVir.

To create the C++ shared library that contains class TestLib:

g++ -shared -fPIC TestLib.cpp -o libTestLib.so

To create the driver app:

g++ -ldl main.cpp -o TestTestLib

To run the sriver test app:

./TestTestLib

Limitations:

1. TestLib must inherit TestVir (header-only) which is part of libTestLib.so. This changes the original artitecture of the shared library.`
2. TestLib.cpp must contain 2 extern "C" functions: create() and destroy(). Can this part be separated from the shared library ???
3. The client app, main.cpp, also needs to include "TestVir.h". So "TestVir.h" plays the role of a common component between the client app and the shared library. Maybe it can be placed into a stubs shared library instead?

