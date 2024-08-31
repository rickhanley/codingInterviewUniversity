#include<stdio.h>
#include<stdbool.h>

int main(void) {
    bool swaps = false;
    int temp = 0;
    int my_array[] = {3, 7, 1, 4, 6, 2};
    int array_length = sizeof(my_array) / sizeof(my_array[0]);

    for(int i = 0; i < array_length; i++) {
        swaps = false;
        for(int j = 0; j < array_length - i - 1; j++){
            if(my_array[j] > my_array[j + 1]){
                temp = my_array[j + 1];
                my_array[j + 1] = my_array[j];
                my_array[j] = temp;
                swaps = true;
            };
        };
        if(swaps == false){
        break;
        };
    };
    for(int i = 0; i < array_length; i++){
        printf("%d\n", my_array[i]);
    };
};