#include <stdio.h>

int main(void){
    
    int arr[] = {9,3,6,1,7,4};
    int arr_length = sizeof(arr) / sizeof(int);

    for(int i = 0; i < arr_length; i++){
        int min = i;

        for(int j = i + 1; j < arr_length; j++){
            if(arr[j] < arr[min]){
                min = j;
            }
        }

        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;


    }

    for(int i = 0; i < arr_length; i++){
        printf("%d\n", arr[i]);
    }

    return 0;
}