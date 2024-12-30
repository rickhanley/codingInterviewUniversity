#include <stdio.h>
#include <stdbool.h>

int main(void){
    int arr[] = {4,2,6,8,1};
    bool swaps = false;
    int temp = 0;
    int length = sizeof(arr) / sizeof(int);

    for(int i = 0; i < length; i++){
        swaps = false;
        // j < lengh - 1 - i:
            // -1 because within the loop we will be comparing the next
            // array element anyway
            // - i because every loop bubbles the highest number to the
            // right of the array, therefore we can decrement by the 
            // value of i - each loop of i gives a number in it's 
            // correct position
        for(int j = 0; j < length - 1 - i; j++){
            if(arr[j + 1] < arr[j]){
                temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
                swaps = true;
            }

        }
        if(swaps == false){
            break;
        }
    }
    for (int i = 0; i < length; i++){
        printf("%d\n", arr[i]);
    }
}