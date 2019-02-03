#include <stdio.h>

char* intToRomanNumeral(int n);

int main(void) {
    int n = 24;
    char* romanNumeral = intToRomanNumeral(n);
    if (romanNumeral != NULL) {
        delete [] romanNumeral;
    }

    return 0;
}

char* intToRomanNumeral(int n) {
    printf("[D] intToRomanNumeral: n=[%d]\n", n);

    if (n <= 0) return NULL;

    int num10s = n / 10;
    n = n % 10;

    int num5s = n / 5;    // 0 or 1
    n = n % 5;

    char* romanNumeral = new char[num10s + num5s + 3 + 1];

    int count = 0;
    for (int i = 0; i < num10s; i++) {
	romanNumeral[count++] = 'X';
    }

    if (num5s) {
	romanNumeral[count++] = 'V';
    }

    switch (n) {
    case 0:
	break;
    case 1:
	romanNumeral[count++] = 'I';
	break;
    case 2:
	romanNumeral[count++] = 'I';
	romanNumeral[count++] = 'I';
	break;
    case 3:
	romanNumeral[count++] = 'I';
	romanNumeral[count++] = 'I';
        romanNumeral[count++] = 'I';
	break;
    case 4:
	romanNumeral[count++] = 'I';
	romanNumeral[count++] = 'V';
	break;
    default:
	break;
    }

    printf("[V] intToRomanNumeral: romanNumeral=[%s]\n", romanNumeral);
    
    return romanNumeral;
}



