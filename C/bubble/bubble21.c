#include <stdio.h>
#include <stdbool.h>

int main(void){

    int arr[] = {8,2,6,1,4,2,3,7,5,0};
    int swaps = false;
    int length = sizeof(arr) / sizeof(int);
    int temp = 0;

    for(int i = 0 ;i < length; i++){
        for(int j = 0; j < length - i; j++){
            if(arr[j + 1] < arr[j]){
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
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