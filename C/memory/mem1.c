#include<stdlib.h>
#include<stdio.h>

int main (void){

    int array_size = 4000;
    int *array = malloc(sizeof(int) * array_size);
    printf("sizeof: %d\n", sizeof(array));



    free(array);
}