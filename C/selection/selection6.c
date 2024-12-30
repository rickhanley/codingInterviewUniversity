// SELECTION SORT
// 


#include <stdio.h>

int main(void) {

    int input[] = {5,1,4,3,2};

    int arr_size = sizeof(input) / sizeof(int);

    for(int i = 0; i < arr_size; i++){
        int current_min = i;

        for(int j = i + 1; j < arr_size; j++){
            if(input[j] < input[i]){
                current_min = j;
            }
        }

        int temp = input[i];
        input[i] = input[current_min];
        input[current_min] = temp;
    }

    for (int i = 0; i < arr_size; i++){
        printf("%d\n", input[i]);
    }
}