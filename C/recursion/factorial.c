#include <stdio.h>

int factorial(int fact);

int main (void){

    int input = 10;
    int result = factorial(input);

    printf("Result: %d\n", result);
    printf("sizeof(int): %d", sizeof(int));

    return 0;
}

int factorial(int n){
    if (n == 1){
        return 1;
    }
    else{
        return n * factorial(n - 1);
    }
}