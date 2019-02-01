#include <stdio.h>
#include <string.h>

void reverseString(char* word);

int main() {
    char word[4] = "abc";
    reverseString(word);
    return 0;
}

void reverseString(char* word) {
    printf("reverseString: input word=[%s]\n", word);
    if (word == NULL) {
	printf("[E] word == NULL !!!");
	return;
    }
    int len = strlen(word);
    if (len <= 1) {
        printf("[W] len <= 1. No need to reverse !");
	return;
    }
    for (int i = 0; i < len/2; i++) {
        char temp = word[i];
	word[i] = word[len-1-i];
	word[len-1-i] = temp;
	i++;
    }
    printf("reverseString: output word=[%s]\n", word);
}

