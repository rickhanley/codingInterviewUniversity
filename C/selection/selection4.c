#include <stdio.h>

int main(void){

    int input[] = {5,1,4,2,3};
    int arr_length = sizeof(input) / sizeof(int);

    for(int i = 0; i < arr_length; i++){
        int current_min_index = i;

        for(int j = i + 1; j < arr_length; j++){
            if(input[j] < input[current_min_index]){
                current_min_index = j;
            }
        }
        
        int temp = input[i];
        printf("%d %d\n", temp, input[i]);
        input[i] = input[current_min_index];
        input[current_min_index] = temp;   

        // int temp = inp[i];
        // inp[i] = inp[min];
        // inp[min] = temp; 

    }

    for (int i = 0; i < arr_length; i++){
        printf("%d\n", input[i]);
    }

}