#include <stdio.h>

int main(void){

    int input[] = {4,1,9,5,8,2};
    int length = sizeof(input) / sizeof(int);

    for(int i = 0; i < length; i++){
        int min = i;
        for(int j = i + 1; j < length; j++){
            if(input[j] < input[min]){
                min = j;
            }
        }
        // int temp = arr[min];
        // arr[min] = arr[i];
        // arr[i] = temp;

        int temp = input[min];
        input[min] = input[i];
        input[i] = temp;
    }

    for(int i = 0; i < length; i++){
        printf("%d\n", input[i]);
    }

    return 0;
}