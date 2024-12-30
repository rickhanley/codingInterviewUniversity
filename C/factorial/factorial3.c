#include <stdio.h>

int fact(int x);

int main(void){
    int input = 8;

    printf("Result: %d", fact(input));

    return 0;
}

int fact(int x){
    if(x == 1){
        return 1;
    }
    else {
        return x * (fact(x- 1));
    }
}