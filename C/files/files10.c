#include <stdio.h>

int main(void){

    char buffer[128];
    int counter = 0;

    FILE* infile = fopen("frankenstein.txt", "r");

    while(fgets(buffer, sizeof(buffer), infile)){
        printf("%s", buffer);
        counter ++;
    }
    fclose(infile);
    printf("Total lines: %d\n", counter);
}