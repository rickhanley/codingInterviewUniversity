#include <stdio.h>

int main(void) {

    long long iterations = 5000000;

    long long running_total;

    for (int i = 0; i < 50000000; i++){
        running_total += i;
    };

    printf("Calc: %ld", (iterations * (iterations + 1)) / 2);

}