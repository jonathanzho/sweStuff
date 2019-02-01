#include <stdio.h>
#include <string.h>

typedef struct Person {
    int age;
    char name[10];
} Person;

int main(void)
{
    printf("TestStructToString: Start\n");

    // Create john Person
    Person johnPerson;
    johnPerson.age = 40;
    printf("johnPerson.age=[%d]\n", johnPerson.age);
    strcpy(johnPerson.name, "John");
    printf("johnPerson.name=[%s]\n", johnPerson.name);

    int struSize = (int) sizeof(Person);
    printf("johnPerson.size=[%d]\n", struSize);

    // john string by memory copy
    char johnMcpyStr[100]; 

    memcpy(johnMcpyStr, &johnPerson, struSize);

    // !!! The printouts may be misleading: length 1
    printf("johnMcpyStr.length=[%d]\n", (int)strlen(johnMcpyStr));
    printf("johnMcpyStr=[%s]\n", johnMcpyStr);

    // back to john Person
    Person johnMcpyPerson;
    memcpy(&johnMcpyPerson, johnMcpyStr, struSize);

    // !!! But the data are correct:
    printf("johnMcpyPerson.age=[%d]\n", johnMcpyPerson.age);
    printf("johnMcpyPerson.name=[%s]\n", johnMcpyPerson.name); 

    // john string by casting 
    char* johnCastStr; 

    johnCastStr = (char *) &johnPerson;

    // !!! The printouts may be misleading: length 1
    printf("johnCastStr.length=[%d]\n", (int)strlen(johnCastStr));
    printf("johnCastStr=[%s]\n", johnCastStr);

    // back to john Person
    Person* johnCastPerson;
    johnCastPerson = (Person*) johnCastStr;

    // !!! But the data are correct:
    printf("johnCastPerson->age=[%d]\n", johnCastPerson->age);
    printf("johnCastPerson->name=[%s]\n", johnCastPerson->name); 

    printf("TestStructToString: End\n");
}


