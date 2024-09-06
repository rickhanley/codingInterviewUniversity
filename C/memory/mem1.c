#include<stdlib.h>
#include<stdio.h>

int main (void){

    int array_size = 400;
    int *array = malloc(sizeof(int) * array_size);
    printf("sizeof: %d\n", array_size / sizeof(array[0]));

    free(array);
    array = NULL;

    if(array == NULL){
        printf("All good!\n");
    };
};