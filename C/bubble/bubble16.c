#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <time.h>

// define array length
#define ARRAY_LENGTH 100000

// function declaration - returns an int POINTER
int *random_ints();

int main (void){

    // true false to determine if swaps happened
    bool swaps = false;

    // declare an int POINTER to receive the POINTER from random_ints
    int *my_array = random_ints();

    // temp int variable to facilitate swapping
    int temp = 0;

    // Bubble sort algorithm

    for (int i = 0; i < ARRAY_LENGTH; i++){
        swaps = false;
        for(int j = 0; j < ARRAY_LENGTH - i - 1; j++){
            if (my_array[j] > my_array[j + 1]){
                temp = my_array[j + 1];
                my_array[j + 1] = my_array[j];
                my_array[j] = temp;
                swaps = true;
            };
        };
        if (swaps == false){
            break;
        };
    };
    for(int i = 0; i < ARRAY_LENGTH; i++){
        printf("%d\n", my_array[i]);
    };

    free(my_array);
}
// Functioan definition
// reurns an int POINTER
int *random_ints(){
    // declare int POINTER to hold the array
    // and malloc the correct size  
    int *random_ints = malloc(sizeof(int) * ARRAY_LENGTH);

    // seed the random function
    srand(time(NULL));

    // declare variables to constrain the random number gen
    // 
    int min = 0;
    int max = 32767;
    int random_num = 0;

    for(int i = 0; i < ARRAY_LENGTH; i++){
        random_ints[i] = random_num = min + rand() % (max - min + 1);
    }

    // Generate some ranomd numbers
    // rand() will generate between 0 and 32767 by default.
    // 

    // for(int i = 0; i < ARRAY_LENGTH; i++){
    //     random_ints[i] = rand() + 1;
    // }

    // return the pointer
    return random_ints;

    // printf("%d\n", random_ints[3]);
    // printf("%d\n", random_ints[99999]);
    // printf("%d\n", random_ints[10000]);
}