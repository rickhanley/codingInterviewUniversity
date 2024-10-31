#include <stdio.h>
#include <stdbool.h>

int main (void) {

    int my_array[] = {7,4,9,1,6};
    int temp = 0;
    bool swaps = false;
    int length = sizeof(my_array) / sizeof(my_array[0]);
    // printf("%d\n", length);

    for (int i = 0; i < length; i++){
        swaps = 0;
        for(int j = 0; j < length - i - 1; j++){
            // printf("%d\n", j);
            if(my_array[j] > my_array[j + 1]){
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
