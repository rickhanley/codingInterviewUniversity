#include <stdlib.h>
#include <stdio.h>
#include <string.h>

int main(void){
    FILE *readptr;
    FILE *writeptr;
    char buffer[30];

    readptr = fopen("wordlist.txt", "r");
    if(readptr != NULL){
        printf("File opened!\n");
    };

    writeptr = fopen("minlengthsix.txt", "w");
    if(readptr != NULL){
        printf("Write file ready!\n");
    };

    while (fgets(buffer, sizeof(buffer), readptr) != NULL) {
        if(strlen(buffer) >= 7){
            // printf("buffer: %s\n", buffer);
            fputs(buffer, writeptr);
        };
    };

    fclose(readptr);
    fclose(writeptr);
    printf("Done\n");

    return 0;
}