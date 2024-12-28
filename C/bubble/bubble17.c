#include <stdio.h>
#include <stdbool.h>

int main (void){

    bool swaps = false;
    int temp = 0;

    int arr[] = {5, 3, 8, 6, 1, 9, 2, 7};

    int size = sizeof(arr) / sizeof(arr[0]);

    for(int i = 0; i < size; i++){
        for(int j = 0; j < size - 1 - i; j++){
            if(arr[j] > arr[j + 1]){
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

    for (int i = 0; i < size; i++){
        printf("%d\n", arr[i]);
    };

    return 0;
}