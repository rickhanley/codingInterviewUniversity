#include <stdio.h>
#include <math.h>
#include <stdbool.h>

#define SIZE 30

int main(void){

    bool primes[SIZE];
    int max = sqrt(SIZE);

    printf("max: %d\n", max);

    for(int i=0; i < SIZE; i++){
        if(i == 0 || i == 1){
            primes[i] = false;
        } else {
            primes[i] = true;
        }
    }

    for(int i = 2; i <= max; i++){
        printf("%d selected\n", i);
        for(int j = i * i; j < SIZE; j+=i){
            printf("j: %d\n", j);
            // if(j == 2 || j == 3) continue;
            printf("knocking out %d\n", j);
            primes[j] = false;
        }
    }

    for(int i = 0; i < SIZE; i++){
        if(primes[i] == true){
            printf("prime: %d\n", i);
        }
    }
    return 0;
}