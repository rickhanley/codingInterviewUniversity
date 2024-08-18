#include <stdio.h>

int main(void) {

    int factorial(int n);

    int n = 15;
    int answer = 0;

    answer = factorial(n);
    printf("answer: %d", answer);

    return 0;
};

int factorial(int n) {
    if(n == 1) {
        return 1;
    }
    else{
        return n * factorial(n - 1);
    };
};