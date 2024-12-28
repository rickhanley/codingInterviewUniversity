#include <stdio.h>

int main (void){

    int width = 7;


    for(int i = 0; i < width; i++){
        // for(int j = i; j > 0; j--){
        //     printf("*");
        // }
        for(int j = 0; j < width; j++){
            // printf("j: %d   i: %d\n", j, i);
            if (j <= i){
                printf("X");
            }
            else{
                printf(" ");
            }
        }
        for(int j = width; j >= 0; j--){
            // printf("j: %d   i: %d\n", j, i);
            if (j > i){
                printf("X");
            }
            else{
                printf(" ");
            }
        }
        // for(int j = width; j > 0; j--){
        //     printf("*");
        // }
        printf("\n");   
    }
}