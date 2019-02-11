#include <stdio.h>

void stampPairing(int a, int b, int n, int* x, int*y);

int main(void) {
    int a = 3;
    int b = 5;
    int x = -1;
    int y = -1;

    for (int n = 8; n <= 100; n++) {
        stampPairing(a, b, n, &x, &y);
	 printf("[V] TestStampPairing: a=[%d], b=[%d], n=[%d], x=[%d], y=[%d]\n", a, b, n, x, y);
    }

    return 0;
}

void stampPairing(int a, int b, int n, int*x, int*y) {
    printf("[D] stampPairing: a=[%d], b=[%d], n=[%d]\n", a, b, n);

    *x = -1;
    *y = -1;

    int xMax = n / a;
    int yMax = n / b;

    if (n % a == 0) {
        *x = xMax;
	*y = 0;
	return;
    }

    if (n % b == 0) {
	*y = yMax;
	*x = 0;
	return;
    }

    for (int yi = 1; yi <= yMax; yi++) {
	if ((n-yi*b) % a == 0) {
	    *y = yi;
	    *x = (n-yi*b) / a;
	    return;
	}
    }
}

