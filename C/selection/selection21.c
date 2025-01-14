#include <stdio.h>

int main(void){

    int arr[] = {4,7,1,9,2,0,3,8};
    int length = sizeof(arr) / sizeof(int);

    for(int i = 0; i < length - 1; i++){
        int min = i;
        for(int j = i + 1; j < length; j++){
            if(arr[j] < arr[min]){
                min = j;
            }
        }

        int temp = arr[min];
        arr[min] = arr[i];
        arr[i] = temp;
    }

    for(int i = 0; i < length; i++){
        printf("%d\n", arr[i]);
    }

    return 0;
}