#include <stdio.h>
#include <stdbool.h>


int main(void){

    int temp = 0;
    bool swaps = false;
    int length = 0;

    int my_array[] = {6,8,2,5,1,5,9,3,1,5,8,4,7,3,7};

    length = sizeof(my_array) / sizeof(int);

    for (int i = 0; i < length; i++){
        swaps = false;
        for (int j = 0; j < length - i - 1; j++){
            if (my_array[j] > my_array[j + 1]){
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
    };

    return 0;
}