#include <stdio.h>

int main(int argc, char *argv[]) {
    // Print the number of arguments
    printf("Number of arguments: %d\n", argc);

    // Loop through all arguments and print them
    for (int i = 0; i < argc; i++) {
        printf("Argument %d: %s\n", i, argv[i]);
    }

    return 0;
}