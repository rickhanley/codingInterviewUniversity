#include <stdio.h>

int minus_10(int input);

int main(void){
    int result = 0;
    result = minus_10(12);
    printf("Result: %d\n", result);

    return 0;
}

int minus_10(int input){
    return input -10;
}