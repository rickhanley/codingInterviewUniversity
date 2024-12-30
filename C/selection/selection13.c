#include <stdio.h>

int main(void){

    int arr[] = {4,2,8,1,9,5};
    int length = sizeof(arr) / sizeof(int);

    for(int i = 0; i < length; i++){
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