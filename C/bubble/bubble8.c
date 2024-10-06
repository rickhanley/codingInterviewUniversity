#include <stdio.h>
#include <stdbool.h>

int main(void){

    int array[]={3,66,44,77,1,23,4,7,9,2,135,1354,9};

    int length = sizeof(array) / sizeof(array[0]);

    int temp = 0;
    bool swaps = false;

    for (int i = 0; i < length; i++){
        swaps = false;
        for (int j = 0; j < length - i - 1; j++){
            if (array[j] > array[j+1]){
                temp = array[j+1];
                array[j+1] = array[j];
                array[j] = temp;
                swaps = true;
            }
        }
        if (swaps = false){
            break;
        }
    }
    for (int i = 0; i < length; i++){
        printf("%d\n", array[i]);
    }
}