#include <stdio.h>

int main(void) {

    int my_array[10][10] = {0};

    for(int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            my_array[i][j] = i;
        };
    };

    printf("%d\n",my_array[9][9]);
    

    return 0;
}