#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main (void){

    int array_size = 350;
    int number = 0;
    int *number2 = &number;

    printf("number 2: %p\n", number2);

    int *my_array = malloc(sizeof(int) * array_size);

    for(int i = 0; i < array_size; i++){
        my_array[i] = i;
    };

    // for(int i = 0; i < array_size; i++){
    //     printf("my_array[%d] = %d\n", i, my_array[i]);
    // };

    int *my_array_2 = malloc(sizeof(int) * array_size);
    long *my_array_3 = malloc(sizeof(long) * array_size);

    memcpy(my_array_2, my_array, (array_size * sizeof(int)));

    for(int i = 0; i < array_size; i++){
        printf("my_array[i] = %ld\n", my_array[i]);
    };
    for(int i = 0; i < array_size; i++){
        printf("my_array_2[i] = %ld\n", my_array_2[i]);
    };
    for(int i = 0; i < array_size; i++){
        my_array_3[i] = my_array[i] * my_array_2[i];  
    };

    for(int i = 0; i < array_size; i++){
        printf("%d x %d = %ld\n", my_array[i], my_array_2[i], my_array_3[i]);
    };




    free(my_array);
    my_array = NULL;
    free(my_array_2);
    my_array_2 = NULL;
    free(my_array_3);
    my_array_3 = NULL;
    return 0;
}