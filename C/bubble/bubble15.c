#include <stdio.h>
#include <stdbool.h>

int main(void){

    bool swaps = false;
    int temp = 0;

    int my_array[] = {3,4,1,2,5}; 

    int length = sizeof(my_array) / sizeof(int);

    for (int i = 0; i < length; i++){
        swaps = false;
        for (int j = 0; j < length - 1 - i; j++){
            if (my_array[j]  > my_array[j + 1]){
                temp = my_array[j + 1];
                my_array[j + 1] = my_array[j];
                my_array[j] = temp;
                swaps = true;
            }
        }
        if (swaps == false){
                break;
        }
    }

    for (int i = 0; i < length; i++){
        printf("%d\n", my_array[i]);
    }

    return 0;
}