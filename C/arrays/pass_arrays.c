#include <stdio.h>
#include <stdlib.h>

int *my_array_gen();

int main(void){

    int *my_array = my_array_gen();
    int *my_array2 = my_array_gen();

    for (int i = 0; i < 100; i++){
        printf("1: %d\n", my_array[i]);
    }
    for (int i = 0; i < 100; i++){
        printf("2: %d\n", my_array2[i]);
    }
free(my_array);
free(my_array2);
my_array = NULL;
my_array2 = NULL;

}

int *my_array_gen(){

    int *array_gen = malloc(100 * sizeof(int));

    if (array_gen == NULL){
        perror("Malloc failed\n");
        exit(EXIT_FAILURE);
    }

    for (int i = 0; i < 100; i++){
        array_gen[i] = i;
    }
    printf("Print from array_gen: %d\n", array_gen[10]);
    return array_gen;
}