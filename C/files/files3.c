#include <stdio.h>

int main(void){

    FILE *file = fopen("greeting.txt", "w");
    if(file == NULL){
        printf("Memory allocation failed\n");
    }

    fprintf(file, "Hello, World!");
    fclose(file);

    return 0;
}