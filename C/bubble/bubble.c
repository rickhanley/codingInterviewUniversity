#include<stdio.h>
#include<stdbool.h>
#include<stdlib.h>

int main(void) {

    bool swaps_made = false;
    int unsorted[1000]; // test data

    for(int i = 0; i < 10; i++){
        unsorted[i] = rand() % 50;
    }

    // for(int i = 0; i < (sizeof(unsorted) / sizeof(unsorted[0])); i++) {
    //     printf("%d\n", unsorted[i]);
    // }

    int temp = 0;
    int array_size = (sizeof(unsorted) / sizeof(int));
    printf("array size: %d", array_size);
    
    
    for(int i = 0; i < array_size; i++) {    
        // swaps_made = false; 
        for(int j = 0; j < array_size - 1 - i; j++) {
                printf("inside main swapping area: i: %d, j: %d\n", i, j);
                temp = unsorted[j];
                unsorted[j] = unsorted[j + 1];
                unsorted[j + 1] = temp;
                swaps_made = true;
        };
        if (swaps_made == false){
                printf("breaking!\n");
                break;
            }
    };
    for(int i = 0; i < (sizeof(unsorted) / sizeof(unsorted[0])); i++) {
        printf("%d\n", unsorted[i]);
    }
    return 0;
}