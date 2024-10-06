#include <stdio.h>
#include <stdbool.h>

int main(void){

    int array[]={4,8,9,22,3,77,44,55,2,454,8,1,3,7,9,1};

    int length = sizeof(array) / sizeof(array[0]);

    printf("%d\n", length);
    int temp = 0;
    bool swaps = false;

    for (int i = 0; i < length; i++){
        printf("%d\n", i);
        
        swaps = false;
        
        for (int j = 0; j < length - 1 - i; j++){
            printf("j - 1 - i: %d\n", j -1 - i);
            printf("j: %d\n", j);
            if (array[j] > array[j + 1]){
                printf("higher\n");
                temp = array[j + 1];
                array[j + 1] = array[j];
                array[j] = temp;
                swaps = true;
            }
            
        }
        if (swaps == false){
                break;
            }
    }
    for (int i = 0; i < length; i++){
        printf("%d\n", array[i]);
    }
}
