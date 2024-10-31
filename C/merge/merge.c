#include <stdio.h>
#include <stdlib.h>

int main(void){

    int array1[5] = {2,4,6,7,9};
    int array2[5] = {1,3,5,8,10};

    int combined_length = sizeof(array1) / sizeof(int) + sizeof(array2) / sizeof(int);

    printf("combined_length: %d\n", combined_length * sizeof(int));

    int *array3 = malloc(combined_length);
    printf("array3 size %d\n", combined_length);

    int array1_index = 0;
    int array2_index = 0;

    for (int i = 0; i < combined_length; i++){

            printf("ar1: %d    ar2: %d\n", array1_index, array2_index);
            if(array1[array1_index] < array2[array2_index]){
                array3[i] = array1[array1_index];
                array1_index++;
            } else {
                array3[i] = array2[array2_index];
                array2_index++;
            };
    };

    for (int i = 0; i < combined_length; i++){
        printf("%d\n", array3[i]);
    }


    free(array3);

    return 0;
}