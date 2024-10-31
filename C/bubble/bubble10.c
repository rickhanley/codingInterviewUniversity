#include <stdio.h>
#include <stdbool.h>

int main(void){

    int array[]={3,2,4,6,4,3,6,8,6,3,3,6,8,5,3,2,4,7,9,5};
    int temp = 0;
    bool swaps = false;

    int length = sizeof(array) / sizeof(int);
    // printf("%d", length);


    for (int i = 0; i < length; i++){
        // printf("i: %d\n", i);
        swaps = false;
        for (int j = 0; j < length - i - 1; j++){
            
            if (array[j] > array[j + 1]){
                temp = array[j + 1];
                array[j + 1] = array[j];
                array[j] = temp;
                swaps = true;
            }
        };
        if (swaps == false){
            break;
        };
    };

    for (int i = 0; i < length; i++){
        printf("%d", array[i]);
        if (i % 3 == 0){
            printf("\n");
        }
    }

    return 0;
}