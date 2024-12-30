#include <stdio.h>
#include <stdbool.h>


int main(void){

    int temp = 0;
    bool swaps = false;
    int arr[] = {9,1,4,6,7,1,2,4,8,2,5,8,2};
    int length = sizeof(arr) / sizeof(int);
    int comps = 0;

    for(int i = 0; i < length; i++){
        swaps = false;
        for(int j = 0; j < length - i - 1; j++){
            if(arr[j + 1] < arr[j]){
                temp = arr[j + 1];
                arr[j + 1] = arr[j];
                arr[j] = temp;
                swaps = true;        
            }
            comps++;
        }
        
        if (swaps == false){
            break;
        }
    }

    for(int i = 0; i < length; i++){
        printf("%d\n", arr[i]);
    }

    printf("\n\nComps %d:", comps);

    return 0;
}