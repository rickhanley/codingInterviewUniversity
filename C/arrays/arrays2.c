#include <stdio.h>
#include <stdlib.h>

int main(void){

    int array_sizing = 150;

    int *my_array = malloc(sizeof(int) * array_sizing);

    for(int i = 0; i < array_sizing; i++){
        my_array[i] = i;
    };

    for(int i = 0; i < array_sizing; i++){
        printf("%d\n", my_array[i] = i);
    }

}