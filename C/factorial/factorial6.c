#include <stdio.h>

int factorial(int x){
    if(x == 1){
        return 1;
    } else {
        return x * factorial(x - 1);
    }
}


int main(void){

    int input = 5;

    printf("%d", factorial(input));

    return 0;
}