#include <stdio.h>
#include <stdbool.h>

int main (void){

    int my_array[]={2,1,4,3,6,5,8,7,10,9};
    bool swaps = false;
    int temp = 0;
    int swap_count = 0;

    int length = sizeof(my_array) / sizeof(int);

    for (int i = 0; i < length; i++){
        for (int j = 0; j < length; j++){
            if (my_array[j] > my_array[j + 1]){
                temp = my_array[j + 1];
                my_array[j + 1] = my_array[j];
                my_array[j] = temp;
                swaps = true;
                swap_count++;
            };
        };
        if (swaps = false){
            break;
        };
    };

    for (int i = 0; i < length; i++){
        printf("%d\n", my_array[i]);
    };

    printf("\nSwap count: %d", swap_count);

    return 0;
}