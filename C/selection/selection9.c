#include <stdio.h>

int main(void){

    int arr[] = {4,2,7,1,3};
    int size = sizeof(arr) / sizeof(int);

    for(int i = 0; i < size; i++){
        int min = i;
        for(int j = i + 1; j < size; j++){
            if(arr[j] < arr[min]){
                min = j;
            }
        }
        // temp gets the value at current min index
        int temp = arr[min];
        // value at current min now gets the value at arr[i]
        arr[min] = arr[i];
        // arr[i] now gets temp
        arr[i] = temp;
    }

    for(int i = 0; i < size; i++){
        printf("%d\n", arr[i]);
    }

}