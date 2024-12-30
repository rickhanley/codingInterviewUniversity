#include <stdio.h>
#include <stdbool.h>

int main(void){

    int arr[] = {3,7,5,3,7,1,9};
    int length = sizeof(arr) / sizeof(int);
    bool swaps = false;
    int temp = 0;

    for(int i = 0; i < length; i++){
        // printf("outer\n");
        swaps = false;
        for(int j = 0; j < length - i - 1; j++){
            // printf("inner\n");
            if(arr[j + 1] < arr[j]){
                // printf("comparing %d   %d\n", arr[j + 1], arr[j]);
                temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
                swaps = true;
            }        
        }
        if (swaps == false){
                break;
            } 
    }

    for(int i = 0; i < length; i++){
        printf("%d\n", arr[i]);
    }

    return 0;
}