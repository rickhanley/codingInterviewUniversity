#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#include<stdlib.h>

int main(void){
    bool swaps = false;
    // int array[] = {16,15,14,13,12,11,10,9,8,7,6,5,4,3,2,1};
    int array[] = {1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16};
    int array_length = sizeof(array) / sizeof(array[0]);
    int temp = 0;
    int swap_count;

    for(int i = 0; i < array_length; i++){
        swaps = false;
        for(int j = 0; j < array_length - i - 1; j++){
            if(array[j] > array[j + 1]){
                temp = array[j];
                array[j] = array[j + 1];
                array[j + 1] = temp;
                swaps = true;
                swap_count++;
            };
        };
        if(swaps == false){
            break;
        };
    };

    for(int i = 0; i < array_length; i++){
        printf("Array position %d:  = %d\n", i, array[i]);
    };
    printf("Swap count: %d\n", swap_count);
};

