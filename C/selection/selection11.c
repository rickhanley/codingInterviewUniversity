#include <stdio.h>

int main(void){

    int input[] = {3,7,5,6,8,1};
    int length = sizeof(input) / sizeof(int);

    for(int i = 0; i < length; i++){
        int min = i;
        for(int j = i + 1; j < length; j++){
            if(input[j] < input[min]){
                min = j;
            }
        }

        int temp = input[min];
        input[min] = input[i];
        input[i] = temp;

    }

    for(int i = 0; i < length; i++){
        printf("%d\n", input[i]);
    }


    return 0;
}