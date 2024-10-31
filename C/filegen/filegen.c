#include <stdio.h>
#include <stdlib.h>

int main(void){

    int max = 5000;
    FILE *fptr = fopen("output.txt", "w");

    if (fptr == NULL){
        printf("File opening error\n");
        return 1;
    }

    int i = max;
    for (int i = max; i > 1; i--){
        fprintf(fptr,"%d\n", i);
    }
    fprintf(fptr,"%d", 1);

    fclose(fptr);
    return 0;
}