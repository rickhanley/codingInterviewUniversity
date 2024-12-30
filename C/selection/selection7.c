#include <stdio.h>

int main(void){

    int input[] = {8,3,6,1,4};
    int arr_size = sizeof(input) / sizeof(int);

    for(int i = 0; i < arr_size; i++){
        int min = i;
        for(int j = i + 1; j < arr_size; j++){
            if(input[j] < input[min]){
                min = j;
            }
        }
        int temp = input[min];
        input[min] = input[i];
        input[i] = temp; 
    }

    for(int i = 0; i < arr_size; i++){
        printf("%d\n", input[i]);
    }
}