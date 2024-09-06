#include <stdio.h>
#include <stdlib.h>

int main (void)
{
    FILE *fptr;
    char buffer[32];
    long counter = 0;

    fptr = fopen("frankenstein.txt", "r");
    if(fptr != NULL){
        printf("File opened!\n");
    };
    // fscanf
    // uses space as default delimeter
    // fscanf((fptr, "%s", buffer) !+ EOF) reads as
    // look for strings in fptr and put them in buffer whilst EOF
    // has not been encountered.
    while(fscanf(fptr, "%s", buffer) != EOF){
        // printf("%s\n", buffer);
        counter++;
    }

    printf("Word count: %d\n", counter);
    return 0;
}