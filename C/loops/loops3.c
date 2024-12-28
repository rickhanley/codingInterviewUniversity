#include <stdio.h>

int main (void){

    int overall = 0;

    for (int i = 0; i < 10; i++){
        printf("%d\n", i);
        for (int j = 0; j < 10; j++){
            printf("    %d\n",j);
            for (int k = 0; k < 10; k++){
            overall ++;
            };
        };   
    };
    printf("Total: %d\n", overall);
    return 0;
};