#include <stdio.h>
#include <stdlib.h>
#include "helpers.h"
#define LENGTH 3

int adder(int x, int y){
    return x + y;
};

int loop_adder(int *x, int *y, int length){
    for(int i = 0; i < length; i++){
        printf("arr1[%d] + arr2[%d] = %d\n", x[i], y[i], (x[i] + y[i]));
    };
}

int main(void){

    int arr1[LENGTH] = {1,2,3};
    int arr2[LENGTH] = {8,9,10};
    int *my_ptr;
    int number = 9;
    char *my_array = "stringliteral";

    my_ptr = &number;

    printf("ptr: %p   number: %d   *ptr: %d\n", my_ptr, number, *my_ptr);

    number = 10;

    printf("ptr: %p   number: %d   *ptr: %d\n", my_ptr, number, *my_ptr);

    printf("Output of function : %d \n", decrementor(number, my_array));
    printf("Value of original variable : %d \n", number);

    printf("Adder of 9 + 11 = %d\n", adder(9, 11));
    loop_adder(arr1, arr2, LENGTH);
}