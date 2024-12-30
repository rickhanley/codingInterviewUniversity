#include <stdio.h>

int main(void){
    int arr[] = {4,2,7,1,9};
    int arr_size = sizeof(arr) / sizeof(int);

    for(int i = 0; i < arr_size; i++){
        int min = i;
        for(int j = i + 1; j < arr_size - 1; j++){
            if(arr[j] < arr[min]){
                min = j;
            }
        }
        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }

    for(int i = 0; i < arr_size; i++){
        printf("%d\n", arr[i]);
    }
}