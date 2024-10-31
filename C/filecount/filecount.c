#include <stdio.h>
#include <stdlib.h>

int main(void){

    FILE *inptr = fopen("data.txt", "r");

    if (inptr == NULL){
        printf("File opening Error\n");
        return 1;
    };

    int counter = 0;
    char buffer[6];
    int num;

    while (fscanf(inptr, "%d,", &num) == 1) {
        counter++;
    }

    printf("number of values in the file: %d\n", counter);

    fclose(inptr);
};