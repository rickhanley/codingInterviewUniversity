#include <stdio.h>

int main(void){

    int input[] = {5,1,3,2,4};

    int arr_length = sizeof(input) / sizeof(int);

    for(int outer_seed = 0; outer_seed < arr_length; outer_seed++){
        int current_min = outer_seed;
        for(int inner_loop = outer_seed + 1; inner_loop < arr_length; inner_loop++){
            if(input[inner_loop] < input[current_min]){
                current_min = inner_loop;
            }
        }

        int temp = input[outer_seed];
        input[outer_seed] = input[current_min];
        input[current_min] = temp;
        
    }
    for(int i = 0; i < arr_length; i++){
        printf("%d\n", input[i]);
    }

}