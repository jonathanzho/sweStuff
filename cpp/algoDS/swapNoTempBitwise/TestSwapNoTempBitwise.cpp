#include <stdio.h>

void swapNoTempBitwise(int* a, int* b);

int main() {
    int a = 2;
    int b = 3;
    printf("[V] TestSwapNoTempBitwise: before: a=[%d], b=[%d]\n", a, b);
    swapNoTempBitwise(&a, &b);
    printf("[V] TestSwapNoTempBitwise: after : a=[%d], b=[%d]\n", a, b);
    
    return 0;
}

void swapNoTempBitwise(int* a, int* b) {
    printf("[D] swapNoTempBitwise: input *a=[%d], *b=[%d]\n", *a, *b);
    if (a == NULL || b == NULL) {
	printf("[E] swapNoTempBitwise: a or b is NULL !!!");
	return;
    }

    *a = *a ^ *b;
    printf("[V] swapNoTempBitwise: step 1 *a=[%d], *b=[%d]\n", *a, *b);

    *b = *a ^ *b;
    printf("[V] swapNoTempBitwise: step 2 *a=[%d], *b=[%d]\n", *a, *b);

    *a = *a ^ *b;
    printf("[V] swapNoTempBitwise: step 3 *a=[%d], *b=[%d]\n", *a, *b);
}

