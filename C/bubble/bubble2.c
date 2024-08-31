// Bubble sort from memory
#include <stdio.h>
#include <stdbool.h>

int main(void){

    int test_array[] = {5,8,2,5,6,4,2,7,9,11};
    int array_length = sizeof(test_array) / sizeof(test_array[0]);
    printf("array_length: %d\n", array_length);

    printf("\n*******Unsorted List************\n");
    for(int i = 0; i < array_length; i++){
        printf("Number: %d\n", test_array[i]);
    };

    int temp = 0; // temp sotrage to faciliate the swapping of numbers
    bool swaps = false; // track if swaps have been made. If not, we're done.


    // Nested loops required
    for(int i = 0; i < array_length; i++){
        printf("i: %d\n", i);
        swaps = false;
        for(int j = 0; j < array_length - i - 1; j++){
            printf("j: %d\n", j);
            if(test_array[j] > test_array[j + 1]){
                printf("%d   %d", test_array[j], test_array[j + 1]);
                temp = test_array[j] ;
                test_array[j] = test_array[j + 1];
                test_array[j + 1] = temp;
                swaps = true;
            };
        };
        if(swaps == false){
            break;
        };
    };
    printf("\n********Sorted List*************\n");
    for(int i = 0; i < array_length; i++){
        printf("Number: %d\n", test_array[i]);
    };
};