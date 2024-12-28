#include <stdio.h>
#include <stdlib.h>

int main(void) {
    char letters[] = {'a', 'z', '\0'}; // Added null terminator for safety.

    // Allocate enough memory for the user input.
    char input[100];  // Fixed-size buffer; increase if needed.
    char encoded[100]={0};


    printf("%c   %d\n", letters[0], letters[0]);
    printf("%c   %d\n", letters[1], letters[1]);

    printf("Enter some text: \n");
    scanf("%99s", input); // Limit input size to avoid buffer overflow.

    printf("You entered: %s\n", input);
    for (int i = 0; input[i] != '\0'; i++){
        encoded[i] = input[i] -1;
    }
    printf("encoded output is: %s", encoded);

    return 0;
}
